def determine_if_umbrella_needed():
    rain_status = input('Is it raining? ').lower()
    if rain_status == 'y':
        print('Take an umbrella')
    else:
        print('You don\'t need an umbrella')


determine_if_umbrella_needed()
