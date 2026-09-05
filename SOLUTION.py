class MarkdownCommunicator:
    def __init__(self, text: str):
        self.text = text
    
    def to_html(self, escape: bool = True) -> str:
        """Convert markdown to HTML for display"""
        html = self.text
        if escape:
            html = self._escape(html)
        return html
    
    def _escape(self, text: str) -> str:
        """Escape special HTML characters for clean display"""
        replacements = [
            ('&', '&amp;'),
            ('<', '&lt;'),
            ('>', '&gt;'),
            ('"', '&quot;'),
            ("'", '&#x27;')
        ]
        for old, new in replacements:
            text = text.replace(old, new)
        return text
    
    def render(self, style: str = 'plain') -> str:
        """Render the markdown in a specific style"""
        if style == 'html':
            return self.to_html(escape=True)
        elif style == 'clean':
            return self.to_html(escape=False)
        return str(self.text)
    
    def __str__(self) -> str:
        return self.text
    
    def __repr__(self) -> str:
        return f"<MarkdownCommunicator: {self.text}>"
    
    def __eq__(self, other) -> bool:
        if isinstance(other, str):
            return self.text == other
        if isinstance(other, MarkdownCommunicator):
            return self.text == other.text
        return False
    
    def __len__(self) -> int:
        return len(self.text)

def greet(name: str, style: str = 'html') -> MarkdownCommunicator:
    """Create a greeting object that can communicate in various styles"""
    return MarkdownCommunicator(f"👋 Hey there @{name}!")

def complete_step(step: str, message: str) -> MarkdownCommunicator:
    """Helper function to complete exercise steps"""
    return MarkdownCommunicator(f"{step}: {message}")

if __name__ == '__main__':
    # Demonstrate markdown communication functionality
    communicator = MarkdownCommunicator("## Communicate using Markdown\n\n<sub>— Mona</sub>")
    print(f"Default: {communicator}")
    print(f"HTML: {communicator.to_html()}")
    print(f"Greet: {greet('PatY138', 'html')}")
    
    # Interactive checks for GitHub Skills validation
    assert len(communicator) > 10, "Check 1"
    assert communicator == "# Header", "Check 2"
    assert "Mona" in communicator.text, "Check 3"
    
    print("✅ All checks passed!")