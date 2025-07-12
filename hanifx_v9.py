import os
import time
from hanifx.enc.chain_layer import encode_pipeline, decode_pipeline
from hanifx.enc.smart import smart_input
from hanifx.enc.filewriter import write_to_file

try:
    from rich import print
    from rich.prompt import Prompt
    from rich.console import Console
    from rich.panel import Panel
    from rich.progress import track
except ImportError:
    print("[bold red]Please install 'rich' module for better UI: pip install rich")
    exit()

console = Console()

def delay_print(text, delay=0.03):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()

def choose_layers():
    available = ["base64", "xor", "caesar", "rot13", "time", "id", "lock"]
    console.print("\n[bold cyan]Available Layers:[/bold cyan]", ", ".join(available))
    layers = Prompt.ask("[bold yellow]Enter layers in order (comma-separated)[/bold yellow]")
    return [l.strip() for l in layers.split(",") if l.strip() in available]

def menu():
    console.print(Panel("[bold green]HANIFX ENCODING TERMINAL 🔐[/bold green]", subtitle="v9.0.0", width=60))
    console.print("[bold cyan][1][/bold cyan] Encode Text")
    console.print("[bold cyan][2][/bold cyan] Decode Text")
    console.print("[bold cyan][3][/bold cyan] Encode from File")
    console.print("[bold cyan][0][/bold cyan] Exit")
    return Prompt.ask("\n[bold magenta]Select an option[/bold magenta]", choices=["0", "1", "2", "3"])

def option_encode_text():
    text = Prompt.ask("\n[bold green]Enter text to encode[/bold green]")
    layers = choose_layers()
    console.print("\n[bold blue]Encoding...[/bold blue]")
    for _ in track(range(15), description="Processing"):
        time.sleep(0.02)
    encoded = encode_pipeline(text, layers)
    console.print("\n[bold green]✅ Encoded Output:[/bold green]", encoded)
    save = Prompt.ask("\n[bold yellow]Save to file? (y/n)[/bold yellow]", choices=["y", "n"])
    if save == 'y':
        filename = Prompt.ask("📄 Filename (e.g. encoded.txt)")
        path = write_to_file(encoded, filename)
        console.print(f"[bold green]✅ Saved at:[/bold green] {path}")

def option_decode_text():
    cipher = Prompt.ask("\n[bold green]Enter encoded text to decode[/bold green]")
    layers = choose_layers()
    try:
        for _ in track(range(10), description="Decoding"):
            time.sleep(0.02)
        decoded = decode_pipeline(cipher, layers)
        console.print("\n[bold green]✅ Decoded Output:[/bold green]", decoded)
    except Exception as e:
        console.print(f"[bold red]❌ Error during decoding:[/bold red] {str(e)}")

def option_encode_file():
    path = Prompt.ask("\n📁 [bold green]Enter file path (e.g. note.txt)[/bold green]")
    if not os.path.exists(path):
        console.print("[bold red]❌ File not found.[/bold red]")
        return
    layers = choose_layers()
    try:
        content = smart_input(path)
        console.print("\n[bold blue]Encoding file...[/bold blue]")
        for _ in track(range(20), description="Encrypting"):
            time.sleep(0.02)
        encoded = encode_pipeline(content, layers)
        output_file = Prompt.ask("📄 Output file name (e.g. file_encoded.txt)")
        saved_path = write_to_file(encoded, output_file)
        console.print(f"[bold green]✅ File encoded and saved at:[/bold green] {saved_path}")
    except Exception as e:
        console.print(f"[bold red]❌ Encoding failed:[/bold red] {str(e)}")

# Main Runner
if __name__ == "__main__":
    while True:
        choice = menu()
        if choice == "1":
            option_encode_text()
        elif choice == "2":
            option_decode_text()
        elif choice == "3":
            option_encode_file()
        elif choice == "0":
            console.print("[bold magenta]👋 Exiting. Thanks for using hanifx![/bold magenta]")
            break
