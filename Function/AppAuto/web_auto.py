import webbrowser


def web_auto(user):
    # Clean up the input to remove any leading/trailing whitespace
    query = user

    # Check if the user intends to visit, launch, or open a website
    if any(action in query for action in ["visit", "launch", "open"]):
        # Extract the site name by removing the action keyword and leading/trailing spaces
        site_name = query.split(" ")[-1]

        # Ensure the site name is provided and not empty
        if site_name:
            # Format the URL (adding www and .com if necessary)
            link = f"https://www.{site_name}.com"
            try:
                # Attempt to open the website
                webbrowser.open(link)
                return f"Opening {link}..."
            except Exception as e:
                return f"Error opening the website: {e}"
        else:
            return "Please specify the website to visit."

    # If no recognized action is found, return a default response
    return "Invalid command. Please use 'visit', 'launch', or 'open' followed by a website name."

