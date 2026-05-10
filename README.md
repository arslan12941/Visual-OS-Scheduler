# Visual OS Scheduler

An educational GUI application that simulates and visualizes CPU scheduling algorithms.

This repository contains a Tkinter-based scheduler GUI and a simple process input generator. It is intended for learning and demonstrating algorithm behavior (FCFS, HPF, RR, SRTN).

## Features
- Simulate scheduling algorithms and visualize scheduling timelines.
- Generate random process workloads using the provided generator.
- Example inputs and expected outputs are included under the `Visual-OS-Scheduler/testcases/` folder.

## Requirements
- Python 3.8 or newer.
- Recommended: create and use a virtual environment.
- Install dependencies (GUI folder requirements):

```bash
python -m pip install -r "Visual-OS-Scheduler/requirements.txt"
```

## Repository layout
- `Visual-OS-Scheduler/scheduler.py` — main scheduler GUI program.
- `Visual-OS-Scheduler/process_generator.py` — simple process generator that writes a compatible `output.txt`.
- `Visual-OS-Scheduler/output.txt`, `Visual-OS-Scheduler/Out.txt` — example outputs.
- `Visual-OS-Scheduler/testcases/` — sample inputs and expected outputs.

## Quick start (GUI)
1. Install dependencies (see above).
2. Run the scheduler GUI:

```bash
python "Visual-OS-Scheduler/scheduler.py"
```

3. In the GUI:
- Click **Select Input File** and choose a plain-text process file (format described below).
- Set **Context Switch Time** and **Quantum Time** as needed.
- Choose an algorithm from the dropdown (`HPF`, `FCFS`, `RR`, `SRTN`).
- Click **Show/Update Graph** to render the schedule.
- Click **Wirte File** to save results to the filename shown (default `Out.txt`).

No stdin redirection is required—the GUI reads the selected file.

## Input file format
The GUI accepts a simple whitespace-delimited format. Either of the following is supported:

- With process count on the first line:

```
<process_count>
<pid> <arrival_time> <run_time> <priority>
<pid> <arrival_time> <run_time> <priority>
...
```

- Or omit the count and list processes directly:

```
<pid> <arrival_time> <run_time> <priority>
<pid> <arrival_time> <run_time> <priority>
```

Example:

```
3
1 0.0 4.0 2
2 1.5 2.0 1
3 3.0 1.0 3
```

`process_generator.py` creates a compatible `output.txt` when given a generator-spec input (first line: process count; second line: mu_arr sigma_arr; third: mu_run sigma_run; fourth: lambda for priority sampling).

## Outputs
- The GUI writes a tabular summary to the output filename (default `Out.txt`) showing waiting time, turnaround time, and weighted turnaround time per process, plus averages.
- A visual timeline is shown inside the application window.

## Testcases
Use the files under `Visual-OS-Scheduler/testcases/` to validate behavior and compare against expected outputs in `Visual-OS-Scheduler/testcases/Scheduler Samples/`.

## Troubleshooting
- If the GUI fails to start, ensure `tkinter` is available on your Python installation (commonly included with standard CPython on Windows).
- If plotting fails, confirm `matplotlib` and `numpy` are installed.

## Contributing
If you plan to publish this repository on GitHub, consider adding a short `CONTRIBUTING.md` and a license. Pull requests and improvements to the visualization or algorithm implementations are welcome.

---
If you want, I can also: add a short example input file under the repo root, add a `LICENSE` file, or create a minimal `CONTRIBUTING.md` before you push to GitHub.

## Included example
An example input file is provided for quick testing:

- `Visual-OS-Scheduler/testcases/example_input.txt` — a 3-process sample compatible with the GUI.

Run the GUI and open this file via **Select Input File** to see the scheduler behavior.

## License
This project is available under the MIT License — see [LICENSE](LICENSE).
