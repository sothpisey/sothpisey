from rich import box
from rich.columns import Columns
from rich.console import Console
from rich.panel import Panel
from rich.tree import Tree

console = Console(record=True, width=100)

about = """\
I'm a self-taught programming enthusiast based in [green link=https://www.google.com/maps/place/Phnom+Penh/@11.545465,104.8804456,12.5z]Phnom Penh[/], Cambodia.
I spend my time exploring software development through hands-on projects, online learning, and personal research. 
I'm passionate about deepening my understanding of programming and building useful, real-world applications.

[bold green]Checkout my website [bold green link=https://sothpisey.dev]sothpisey.dev[/]"""

panel = Panel.fit(
    about, box=box.DOUBLE, border_style="green", title="[b]Hi there", width=80
)

console.print(panel)

CONSOLE_HTML_FORMAT = """\
<pre style="font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace">{code}</pre>
"""

console.save_html("README.md", inline_styles=True, code_format=CONSOLE_HTML_FORMAT)