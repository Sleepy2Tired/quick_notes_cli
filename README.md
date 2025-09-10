# Quick Notes CLI
A fast and efficient command-line tool for capturing short notes.

## Features
- Simple and intuitive command-line interface
- Quick note capture and retrieval
- Supports markdown formatting for notes
- Lightweight and fast with minimal dependencies
- Cross-platform compatibility

## Quickstart
To get started with Quick Notes CLI, follow these steps:

### Installation
You can install Quick Notes CLI using npm:

```bash
npm install -g quick-notes-cli
```

### Running the Application
After installation, you can start using the tool by running:

```bash
quick-notes
```

## Usage Examples
- **Add a new note:**
  ```bash
  quick-notes add "Remember to review the project requirements."
  ```

- **List all notes:**
  ```bash
  quick-notes list
  ```

- **Retrieve a specific note by ID:**
  ```bash
  quick-notes get 1
  ```

- **Delete a note:**
  ```bash
  quick-notes delete 1
  ```

## Configuration
Quick Notes CLI stores notes in a local file. You can configure the storage path by setting the `NOTES_PATH` environment variable:

```bash
export NOTES_PATH="/path/to/your/notes.json"
```

## Roadmap
- [ ] Implement search functionality
- [ ] Add tagging support for notes
- [ ] Enhance markdown rendering
- [ ] Improve user documentation

## FAQ
**Q: Can I use Quick Notes CLI without Node.js?**  
A: No, Quick Notes CLI requires Node.js to run.

**Q: Is my data secure?**  
A: Yes, your notes are stored locally and not shared with any external service.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.