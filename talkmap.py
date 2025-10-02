import glob
import getorg
from geopy import Nominatim
import os
import traceback
import time

# Use absolute path for the talks directory
g = glob.glob("/Users/ctsl28/PD/mwiet.github.io/_talks/*.md")

geocoder = Nominatim(user_agent="talk-map-generator", timeout=20)
output_dict = {}

for file in g:
    with open(file, 'r') as f:
        lines = f.read()
        
        # Extract location
        if lines.find('location: "') > 1:
            loc_start = lines.find('location: "') + 11
            lines_trim = lines[loc_start:]
            loc_end = lines_trim.find('"')
            location = lines_trim[:loc_end]
        else:
            continue

        # Extract venue
        if lines.find('venue: "') > 1:
            venue_start = lines.find('venue: "') + 8
            lines_trim = lines[venue_start:]
            venue_end = lines_trim.find('"')
            venue = lines_trim[:venue_end]
        else:
            venue = "Unknown Venue"

        # Extract title
        if lines.find('title: "') > 1:
            title_start = lines.find('title: "') + 8
            lines_trim = lines[title_start:]
            title_end = lines_trim.find('"')
            title = lines_trim[:title_end]
        else:
            title = "Untitled"

        # Get the filename without extension for the ID
        talk_id = os.path.splitext(os.path.basename(file))[0]

        # Geocode the location
        try:
            geo_location = geocoder.geocode(location)
            if geo_location:
                # Create a link with the venue and title
                link_text = f"{venue}"
                popup_html = f'<a href="/talks/#{talk_id}" target="_top">{link_text}</a>'
                
                # Create a unique key for each talk
                new_key = f"{popup_html}<br>{location}"
                
                output_dict[new_key] = geo_location
            else:
                print(f"Could not geocode {location}")
                continue
        except Exception as e:
            print(f"Could not geocode {location}: {e}")
            print(f"Exception type: {type(e)}")
            traceback.print_exc()
            continue
        
        time.sleep(1)


# Generate the map
m = getorg.orgmap.create_map_obj()
# Use absolute path for the output folder
getorg.orgmap.output_html_cluster_map(output_dict, folder_name="/Users/ctsl28/PD/mwiet.github.io/talkmap", hashed_usernames=False)