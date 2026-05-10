# Visual OS Scheduler

A simple educational project for simulating and visualizing CPU scheduling algorithms. This repository contains a scheduler implementation and a process generator along with sample testcases and outputs.

**Features**
- **Simulates**: various scheduling algorithms (implementation in [scheduler.py](scheduler.py)).
- **Input generator**: create process inputs using [process_generator.py](process_generator.py).
- **Testcases**: sample inputs and expected outputs in the `testcases/` folder.

**Requirements**
- Python 3.8+ (use `python --version` to check).
- Install dependencies from [requirements.txt](requirements.txt) if present:

```
python -m pip install -r requirements.txt
```

**Repository layout**
- [scheduler.py](scheduler.py) — main scheduler program.
- [process_generator.py](process_generator.py) — optional input generator.
- `Out.txt`, `output.txt` — example output files produced by the programs.
- `testcases/` — contains sample inputs and expected outputs.

**Quick Usage**

1. (Optional) Generate input samples:

```
python process_generator.py
```

2. Run the scheduler. Depending on how `scheduler.py` is implemented it may read from a file or stdin. Common ways to run:

```
python scheduler.py
# or, if it reads from a file:
python scheduler.py testcases/schdinput.txt
# or via stdin redirection:
python scheduler.py < testcases/schdinput.txt > output.txt
```

3. Check outputs in `output.txt` or `Out.txt`, or the printed console output.

**Testcases & Samples**
- Use the files in `testcases/Generator Samples/` and `testcases/Scheduler Samples/` to validate behavior.
- Compare generated output with `testcases/Scheduler Samples/` expected outputs (e.g., `FCFSout.txt`, `RRout.txt`).

**Notes & Troubleshooting**
- If `scheduler.py` expects command-line arguments, open the file to see its expected parameters and adapt the commands above accordingly.
- If you see missing dependencies, install them via `pip` and retry.

**Next steps**
- Run the scheduler with a sample input to confirm outputs.
- Add example command-line argument documentation inside `scheduler.py` or this README after confirming its interface.

---
If you want, I can run a quick inspection of `scheduler.py` to extract exact command-line flags and update this README with precise run examples.
