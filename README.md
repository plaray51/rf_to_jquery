# RichFaces to jQuery Converter

This Python script converts RichFaces 3.3 components to equivalent jQuery-compatible HTML/CSS/JavaScript.

## Features

- **Conversion Rules**: Converts RichFaces tags such as `<rich:dataTable>`, `<rich:column>`, `<rich:panel>`, `<rich:calendar>`, etc., to HTML tags with jQuery equivalents.
- **Dynamic Content Handling**: Converts dynamic content expressions like `#{item.name}` within `<rich:column>` tags to appropriate HTML elements.
- **Button and AJAX Handling**: Converts `<rich:ajaxButton>`, `<rich:commandButton>`, and `<rich:button>` tags to jQuery-based `<button>` elements with AJAX functionality.
- **Input and Form Handling**: Converts `<h:form>`, `<h:inputText>`, `<h:inputTextarea>`, `<h:commandButton>`, `<h:outputText>`, `<h:selectOneMenu>`, etc., to standard HTML form elements.
- **Extensible**: Easily extendable with additional conversion rules for other RichFaces tags or specific application requirements.

## Usage

1. **Input**: Provide your RichFaces 3.3 code snippet in the input text area.
2. **Convert**: Click the "Convert" button to generate the jQuery-compatible code in the output text area.
3. **Copy and Use**: Copy the converted code for integration into your jQuery-based application.

## Prerequisites

- Python 3.x installed on your system.
- tkinter library for Python (standard in most Python installations).

## Installation

No installation required. Simply clone the repository or download the script to use.

## Known Issues

- Conversion may not cover all edge cases of RichFaces 3.3 syntax.
- Specific application requirements may necessitate additional custom conversion rules.

## Contributing

Contributions are welcome! Please feel free to fork the repository and submit pull requests to enhance the converter.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Built with Python and tkinter.
- Inspired by the need to modernize RichFaces 3.3 applications.
