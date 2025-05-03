> here, under maze.py, you'll also find a good use of the robust 'from pathlib import Path' -> 'script_path = Path(__file__).parent' from keith latest tips
> 		(refer to the 'Keith New Tips' repository) 


> under 'clue.py', we're using the 'termcolor' module supporting user defined color for any text print to console :)
> . e.g. >> import termcolor / >> termcolor.cprint(f"{symbol}: YES", "green")

> check on your aliases by: > git config --get-regexp ^alias
> chec kon  a specific alise by: > git config --get alias.[YOUR_ALIAS]  