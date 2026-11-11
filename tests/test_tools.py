import importlib.util
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / "proyectos"


def load(folder, filename):
    spec = importlib.util.spec_from_file_location(folder, ROOT / folder / filename)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class NewPrograms(unittest.TestCase):
    def test_sensor_missing_and_nonfinite_readings(self):
        module = load("sensor-analysis", "analyze.py")
        with tempfile.TemporaryDirectory() as directory:
            file = Path(directory) / "sensor.csv"
            file.write_text("y_V\n1\n3\n2\n", encoding="utf8")
            self.assertEqual(module.summarize(file, "y_V")["median"], 2)
            file.write_text("y_V\nnan\n", encoding="utf8")
            with self.assertRaises(ValueError):
                module.summarize(file, "y_V")

    def test_expenses_decimal_and_validation(self):
        module = load("expense-summary", "expenses.py")
        with tempfile.TemporaryDirectory() as directory:
            file = Path(directory) / "expenses.csv"
            file.write_text("category,amount\nfood,0.10\nfood,0.20\n", encoding="utf8")
            self.assertEqual(str(module.summarize(file)["food"]), "0.30")
            file.write_text("category,amount\nfood,-1\n", encoding="utf8")
            with self.assertRaises(ValueError):
                module.summarize(file)

    def test_checksum_does_not_change_file(self):
        module = load("file-checksums", "checksums.py")
        with tempfile.TemporaryDirectory() as directory:
            file = Path(directory) / "hello.txt"
            file.write_bytes(b"hello")
            self.assertEqual(module.manifest(directory)["hello.txt"], "2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824")
            self.assertEqual(file.read_bytes(), b"hello")

    def test_resistor(self):
        module = load("resistor-colors", "resistor.py")
        self.assertEqual(module.decode("brown", "black", "red", "gold"), (1000, 5))
        with self.assertRaises(ValueError):
            module.decode("black", "black", "red", "gold")

    def test_weights(self):
        module = load("weighted-grades", "grades.py")
        self.assertEqual(module.weighted_mean([(80, 40), (100, 60)]), 92)
        with self.assertRaises(ValueError):
            module.weighted_mean([(80, 30), (100, 60)])


if __name__ == "__main__":
    unittest.main(verbosity=2)
