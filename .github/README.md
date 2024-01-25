<div align="center">

<h1>📝 Marks Analyzer </h1>

A small python script to analyze excel files containg marks and ID numbers, and
provide statistics

Current version: 1.0
</div>

---

# Usage

(1) After cloning the repository, install the necessary package globally or
in an active virtual environment:

```bash
pip install -r requirements.txt
```

(2) Run the main script with the `--help` flag to see further instructions

```bash
python main.py --help
```

---

# Note

The app supports displaying custom statistics for your friends. To use this feature,
create a file named `friends.json` in the CWD, with the following contents:

```javascript
{
    "<Full name>": {
        "ID": "<String>",
        "alternateNames": ["<String>", "<String>", ...]
    },
    ...
}
```

The program will successfully parse the JSON data and give the corresponding
details from the passed spreadsheet. You can pass any name inside `alternateNames`
when prompted, instead of typing the ID everytime.

---
Project started on: 21/01/2024

(v1.0) First functional version completed on: 24/01/2024
