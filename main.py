def get_full_name(first_name:str, last_name:str):
    full_name = first_name.title()+" "+last_name.title()
    return full_name




if __name__ == '__main__':
    print(get_full_name("samitha","athurupana"))