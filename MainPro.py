import options

# Main programme
while True:
    options.main_menu()
    opt = input("\n\tType the option you want : ")
    opt = opt.upper()
    if opt == 'ADD':
        options.add()
    elif opt == 'DDD':
        options.ddd()
    elif opt == 'UDD':
        options.udd()
    elif opt == 'VCT':
        options.vct()
    elif opt == 'SRR':
        options.srr()
    elif opt == 'VRL':
        options.vrl()
    elif opt == 'STF':
        options.stf()
    elif opt == 'RFF':
        options.rff()
    elif opt == 'ESC':
        options.esc()
        break
    else:
        print("\nInvalid option, Enter a valid option again")
        continue
