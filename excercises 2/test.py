dictM={1:"cheese pizza",2:"mac n cheese",3:"sloppy joe"}
choice=int(input(f"choose the option you wish based on the correlating number \n{dictM}"))
try:
        if not choice in dictM.keys:
            raise ValueError("not a menue choice")
except ValueError as e:
        print(e)