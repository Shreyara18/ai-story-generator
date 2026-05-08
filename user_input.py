def get_user_inputs():

    print("!!!!!!!!!    Welcome to the Personalized Story Generator !!!!!!!!!\n ")
    print("Please provide the following details to create your unique story:\n")

    fcharacter_name = input(

        "Enter the main character's name: "
    )

    scharacter_name = input(

        "Enter the supporting character's name: "
    )

    setting = input(

        "Enter the setting of the story (eg. Ancient Kingdom, Space Station, etc..): "
    )

    genre = input(

        "Enter the genre of the story (e.g., fantasy, sci-fi, romance): "
    )

    return fcharacter_name, scharacter_name, setting, genre