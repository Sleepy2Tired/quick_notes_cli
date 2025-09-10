from __future__ import annotations
import argparse
from datetime import datetime
from pathlib import Path
import sys

NOTES_FILE = Path(__file__).parent / "notes.md"

HEADER = """# Quick Notes

A lightweight, timestamped notes file.

"""

def ensure_file():
    if not NOTES_FILE.exists():
        NOTES_FILE.write_text(HEADER, encoding="utf-8")

def timestamp() -> str:
    # ISO-like with local time
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def append_note(text: str) -> None:
    ensure_file()
    with NOTES_FILE.open("a", encoding="utf-8") as f:
        f.write(f"- [{timestamp()}] {text}\n")

def read_notes() -> list[str]:
    if not NOTES_FILE.exists():
        return []
    lines = NOTES_FILE.read_text(encoding="utf-8").splitlines()
    # skip header lines that start with '#' or are blank
    return [ln for ln in lines if ln.strip() and not ln.startswith("#")]

def cmd_add(args):
    text = " ".join(args.text).strip()
    if not text:
        print("Nothing to add. Usage: add \"your note here\"")
        return 1
    append_note(text)
    print("✅ Saved.")
    return 0

def cmd_list(_args):
    notes = read_notes()
    if not notes:
        print("No notes yet. Add one with: python main.py add \"your note\"")
        return 0
    for i, ln in enumerate(notes, start=1):
        print(f"{i:>3}. {ln}")
    return 0

def cmd_search(args):
    q = " ".join(args.query).strip().lower()
    if not q:
        print("Provide a search term. Example: search focus")
        return 1
    notes = read_notes()
    matches = [ln for ln in notes if q in ln.lower()]
    if not matches:
        print("No matches.")
        return 0
    for i, ln in enumerate(matches, start=1):
        print(f"{i:>3}. {ln}")
    return 0

def cmd_stats(_args):
    notes = read_notes()
    total = len(notes)
    by_day = {}
    for ln in notes:
        # line looks like: "- [YYYY-MM-DD HH:MM:SS] text"
        try:
            date_part = ln.split("]")[0].split("[", 1)[1]
            day = date_part.split(" ")[0]
            by_day[day] = by_day.get(day, 0) + 1
        except Exception:
            pass
    print(f"Total notes: {total}")
    if by_day:
        print("By day:")
        for day in sorted(by_day):
            print(f"  {day}: {by_day[day]}")
    return 0

def build_parser():
    p = argparse.ArgumentParser(
        prog="quick-notes",
        description="Tiny CLI to add/list/search timestamped notes in notes.md",
    )
    sub = p.add_subparsers(dest="cmd", required=True)

    a = sub.add_parser("add", help='Add a note. Example: add "ship the MVP"')
    a.add_argument("text", nargs=argparse.REMAINDER)
    a.set_defaults(func=cmd_add)

    l = sub.add_parser("list", help="List all notes")
    l.set_defaults(func=cmd_list)

    s = sub.add_parser("search", help="Search notes (case-insensitive)")
    s.add_argument("query", nargs=argparse.REMAINDER)
    s.set_defaults(func=cmd_search)

    st = sub.add_parser("stats", help="Show totals and per-day counts")
    st.set_defaults(func=cmd_stats)

    return p

def main(argv=None):
    argv = argv if argv is not None else sys.argv[1:]
    parser = build_parser()
    args = parser.parse_args(argv)
    return args.func(args)

if __name__ == "__main__":
    raise SystemExit(main())
