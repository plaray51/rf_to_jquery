import tkinter as tk
from tkinter import scrolledtext
import re

class RichFacesToJQueryConverter:
    def __init__(self):
        self.conversion_rules = [
            # Datatable and Columns
            (r'<rich:dataTable([^>]*)>', r'<table\1 class="datatable">', r'</rich:dataTable>', r'</table>'),
            (r'<rich:column([^>]*)>', r'<td\1>', r'</rich:column>', r'</td>'),
            (r'<rich:columnGroup([^>]*)>', r'<colgroup\1>', r'</rich:columnGroup>', r'</colgroup>'),
            (r'<rich:subTable([^>]*)>', r'<tbody\1>', r'</rich:subTable>', r'</tbody>'),
            # Panel
            (r'<rich:panel([^>]*) header="([^"]*)">', r'<div\1 class="panel"><div class="panel-header">\2</div>', r'</rich:panel>', r'</div>'),
            (r'<rich:panelMenu([^>]*)>', r'<div\1 class="panel-menu">', r'</rich:panelMenu>', r'</div>'),
            (r'<rich:panel([^>]*)>', r'<div\1 class="panel">', r'</rich:panel>', r'</div>'),
            (r'<rich:panelGrid([^>]*)>', r'<div\1 class="panel-grid">', r'</rich:panelGrid>', r'</div>'),
            (r'<rich:togglePanel([^>]*)>', r'<div\1 class="toggle-panel">', r'</rich:togglePanel>', r'</div>'),
            # Buttons
            (r'<rich:ajaxButton\s+id="([^"]+)"\s+value="([^"]+)"\s+action="([^"]+)"\s*/>',
             r'<button id="\1" type="button">\2</button>\n<script>\n$("#\1").click(function() {\n  $.ajax({url: "\3", success: function(result) {\n    // Handle success\n  }});\n});\n</script>', '', ''),
            (r'<rich:commandButton([^>]*)>', r'<button\1>', r'</rich:commandButton>', r'</button>'),
            (r'<rich:button\s+id="([^"]+)"\s+value="([^"]+)"\s*/>', r'<button id="\1" type="button">\2</button>', '', ''),
            # Messages
            (r'<rich:messages([^>]*)>', r'<div\1 class="messages">', r'</rich:messages>', r'</div>'),
            (r'<rich:message([^>]*)>', r'<div\1 class="message">', r'</rich:message>', r'</div>'),
            # Tabs
            (r'<rich:tabPanel([^>]*)>', r'<div\1 class="tab-panel">', r'</rich:tabPanel>', r'</div>'),
            (r'<rich:tab([^>]*)>', r'<div\1 class="tab">', r'</rich:tab>', r'</div>'),
            # Toolbars
            (r'<rich:toolBar([^>]*)>', r'<div\1 class="toolbar">', r'</rich:toolBar>', r'</div>'),
            (r'<rich:toolBarGroup([^>]*)>', r'<div\1 class="toolbar-group">', r'</rich:toolBarGroup>', r'</div>'),
            # Calendar
            (r'<rich:calendar([^>]*)\s*/>', r'<input type="text"\1 class="calendar"/>', '', ''),
            # Menus
            (r'<rich:dropDownMenu([^>]*)>', r'<div\1 class="dropdown-menu">', r'</rich:dropDownMenu>', r'</div>'),
            (r'<rich:menuItem([^>]*)\s*/>', r'<div\1 class="menu-item"></div>', '', ''),
            (r'<rich:menuSeparator([^>]*)>', r'<hr\1>', '', ''),
            (r'<rich:contextMenu([^>]*)>', r'<div\1 class="context-menu">', r'</rich:contextMenu>', r'</div>'),
            # Tree
            (r'<rich:treeNode([^>]*)>', r'<li\1 class="tree-node">', r'</rich:treeNode>', r'</li>'),
            (r'<rich:tree([^>]*)>', r'<ul\1 class="tree">', r'</rich:tree>', r'</ul>'),
            # Other
            (r'<rich:accordion([^>]*)>', r'<div\1 class="accordion">', r'</rich:accordion>', r'</div>'),
            (r'<rich:accordionItem([^>]*)>', r'<div\1 class="accordion-item">', r'</rich:accordionItem>', r'</div>'),
            (r'<rich:toolTip([^>]*)>', r'<div\1 class="tooltip">', r'</rich:toolTip>', r'</div>'),
            (r'<rich:modalPanel([^>]*)>', r'<div\1 class="modal">', r'</rich:modalPanel>', r'</div>'),
            (r'<rich:progressBar([^>]*)>', r'<div\1 class="progress-bar">', r'</rich:progressBar>', r'</div>'),
            (r'<rich:editor([^>]*)>', r'<textarea\1 class="editor"></textarea>', '', ''),
            (r'<rich:fileUpload([^>]*)>', r'<input type="file"\1 class="file-upload"/>', '', ''),
            (r'<rich:orderingList([^>]*)>', r'<div\1 class="ordering-list">', r'</rich:orderingList>', r'</div>'),
            (r'<rich:listShuttle([^>]*)>', r'<div\1 class="list-shuttle">', r'</rich:listShuttle>', r'</div>'),
            (r'<rich:inplaceInput([^>]*)>', r'<input\1 class="inplace-input"/>', '', ''),
            (r'<rich:toggleControl([^>]*)>', r'<div\1 class="toggle-control">', r'</rich:toggleControl>', r'</div>'),
            (r'<rich:focus([^>]*)>', r'<div\1 class="focus">', r'</rich:focus>', r'</div>'),
            (r'<rich:graphValidator([^>]*)>', r'<div\1 class="graph-validator">', r'</rich:graphValidator>', r'</div>'),
        ]

        self.specific_patterns = [
            (r'<f:facet\s+name="header">', r'<th>', r'</f:facet>', r'</th>'),
            (r'<a4j:outputPanel([^>]*)>', r'<div\1>', r'</a4j:outputPanel>', r'</div>'),
            (r'<a4j:commandButton([^>]*)>', r'<button\1>', r'</a4j:commandButton>', r'</button>'),
            (r'<a4j:support([^>]*)>', r'<script\1>', r'</a4j:support>', r'</script>'),
            (r'<a4j:region([^>]*)>', r'<div\1>', r'</a4j:region>', r'</div>'),
            (r'<h:form([^>]*)>', r'<form\1>', r'</h:form>', r'</form>'),
            (r'<h:inputText([^>]*)>', r'<input type="text"\1/>', '', ''),
            (r'<h:inputTextarea([^>]*)>', r'<textarea\1>', r'</h:inputTextarea>', r'</textarea>'),
            (r'<h:commandButton([^>]*)>', r'<button\1>', r'</h:commandButton>', r'</button>'),
            (r'<h:outputText([^>]*)>', r'<span\1>', r'</h:outputText>', r'</span>'),
            (r'<h:selectOneMenu([^>]*)>', r'<select\1>', r'</h:selectOneMenu>', r'</select>'),
            (r'<f:selectItem([^>]*)>', r'<option\1>', r'</f:selectItem>', r'</option>'),
            (r'<h:selectManyCheckbox([^>]*)>', r'<div\1 class="select-many-checkbox">', r'</h:selectManyCheckbox>', r'</div>'),
        ]

    def convert(self, jsf_code):
        # Apply conversion rules for standard RichFaces tags
        for open_tag_pattern, open_tag_replacement, close_tag_pattern, close_tag_replacement in self.conversion_rules:
            jsf_code = re.sub(open_tag_pattern, open_tag_replacement, jsf_code, flags=re.DOTALL | re.IGNORECASE)
            jsf_code = re.sub(close_tag_pattern, close_tag_replacement, jsf_code, flags=re.DOTALL | re.IGNORECASE)

        # Apply conversion rules for specific patterns like facets and A4J tags
        for open_tag_pattern, open_tag_replacement, close_tag_pattern, close_tag_replacement in self.specific_patterns:
            jsf_code = re.sub(open_tag_pattern, open_tag_replacement, jsf_code, flags=re.DOTALL | re.IGNORECASE)
            jsf_code = re.sub(close_tag_pattern, close_tag_replacement, jsf_code, flags=re.DOTALL | re.IGNORECASE)

        # Handle dynamic content like #{item.name} within rich:column
        jsf_code = re.sub(r'#{item\.(\w+)}', r'<span id="item_\1">[\1]</span>', jsf_code)


        # Remove unwanted 'value' attributes and self-closing tag errors
        jsf_code = re.sub(r'value="[^"]*"\s*/>', r'/>', jsf_code)

        return jsf_code

def convert_code():
    input_code = input_text.get("1.0", tk.END)
    converter = RichFacesToJQueryConverter()
    output_code = converter.convert(input_code)
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, output_code)

# Create the main window
root = tk.Tk()
root.title("RichFaces to jQuery Converter")

# Create input text area
input_label = tk.Label(root, text="RichFaces 3.3 Code")
input_label.pack()
input_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=80, height=10)
input_text.pack()

# Create convert button
convert_button = tk.Button(root, text="Convert", command=convert_code)
convert_button.pack()

# Create output text area
output_label = tk.Label(root, text="Converted jQuery Code")
output_label.pack()
output_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=80, height=10)
output_text.pack()

# Run the application
root.mainloop()