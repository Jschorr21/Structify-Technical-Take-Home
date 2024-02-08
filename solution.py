import argparse
import json

def is_in_between(a, x, y):
    """Check if a number 'a' is between 'x' and 'y'."""
    return x < a < y

def count_intersections(chord_data):
    """
    Counts the number of intersections between chords defined by their radian measures.
    
    Parameters:
    chord_data (tuple): A tuple containing two lists, one with measures and one with labels.
    
    Prints the total count of intersections.
    """
    # Extract measures and labels from the chord_data.
    measures = chord_data[0]
    labels = chord_data[1]
    chord_dict = {}
    
    # Iterate over the angles and labels to build a dictionary that maps
    # each chord to its start and end angles.
    for angle, id in zip(measures, labels):
        chord_num = id.split('_')[1]  # Extracts chord number from label
        if chord_num not in chord_dict:
            # If the chord is not in the dictionary, initialize with the angle.
            chord_dict[chord_num] = [angle]
        else:
            # If the chord is already in the dictionary, add the angle and sort.
            start, end = sorted(chord_dict[chord_num] + [angle])
            chord_dict[chord_num] = [start, end]
    
    # Convert the list of angles to tuples and keys to integers.
    chord_dict = {int(key): tuple(value) for key, value in chord_dict.items()}

    # Initialize the count of intersections.
    chords_num = len(chord_dict)
    intersection_count = 0
    
    # loop through the chords to count intersections.
    for i in range(1, chords_num+1):
        for j in range(i+1, chords_num+1):
            # Extract start and end angles for both chords.
            cur_start, cur_end = chord_dict[i]
            next_start, next_end = chord_dict[j]
            
            # Check if one end of a chord is between the ends of another chord
            # and increment the count if so.
            if is_in_between(cur_start, next_start, next_end) != is_in_between(cur_end, next_start, next_end):
                intersection_count += 1
    
    # Print the total count of intersections.
    print(intersection_count)
        

def main():
    # Create the parser
    parser = argparse.ArgumentParser(description='Count intersections of chords in a circle.')
    # Add argument for the chord_data in JSON format
    parser.add_argument('chord_data', type=str, help='JSON chord_data containing two lists: measures and labels. For example: \'{"measures": [m1, m2, ...], "labels": [l1, l2, ...]}\'')
    
    # Parse arguments
    args = parser.parse_args()

    # Parse the JSON chord_data
    try:
        chord_data = json.loads(args.chord_data)
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON chord_data: {e}")
        return

    measures = chord_data.get('measures')
    labels = chord_data.get('labels')

    # Ensure that the measures and labels are present and of the same length
    if not measures or not labels:
        print("Error: JSON chord_data must include 'measures' and 'labels' lists.")
        return
    if len(measures) != len(labels):
        print("Error: The number of measures and labels must be the same.")
        return

    # Call the count_intersections function with  measures and labels
    count_intersections([measures, labels])

# Entry point 
if __name__ == "__main__":
    main()
