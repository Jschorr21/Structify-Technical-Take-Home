# Structify-Technical-Take-Home
## Chord Intersection Counter

## Description
This Python script counts the number of intersections between chords within a circle. Each chord is defined by two points on the circumference of the circle, represented by their radian measures, and identified by a unique label.

## Algorithm
The script operates as follows:
1. **Input Parsing**: Accepts a JSON string input containing two lists: `measures` (radian measures of chord endpoints) and `labels` (identifying labels for chord start and end points).
2. **Dictionary Construction**: Iterates over the `measures` and `labels` to build a dictionary (`chord_dict`) mapping each chord to a tuple with its start and end angles.
3. **Intersection Counting**: Iterates through `chord_dict` to count how many times one chord's end is between the start and end of another chord, indicating an intersection.

## Requirements
- Python 3.x
- No external libraries required beyond the Python Standard Library.

## How to Run
1. **Prepare Your Input**: Format your chord measures and labels into a JSON string. The input should look like this: `'{"measures": [0.78, 1.47, 1.77, 3.92], "labels": ["s_1", "s_2", "e_1", "e_2"]}'`, where `measures` are the radian measures of chord endpoints and `labels` are corresponding identifiers starting with `s_` for start and `e_` for end.

2. **Execute the Script**: Run the script from the command line by passing the JSON input as an argument. Use the following command format:

   ```sh
   python solution.py '{"measures": [m1, m2, ...], "labels": ["l1", "l2", ...]}'

##Output
The script prints the total count of intersections among the chords defined by the input.

##Big-O Runtime Analysis
I will break down the algorithm into a few parts in order to analyze its total runtime.
1. **Construction of `chord_dict`:** Iterating over each radian measure and label using a for loop has a complexity of `O(n)`, and each iteration performs only constant (`O(1)`) operations. Each sort is also `O(1)` since there is a maximum of two items in each chord list. This portion of the algorithm is `O(n)`.
2. **Converting Lists to Tuples and Keys to Integers:** The loop converting each list to a tuple and each key to an integer perform constant operations for each chord, which would be n/2 chords assuming the number of measures/labels is n. This portion of the algorithm is also `O(n)`.
3. **Counting Intersections:** The nested loop structure iterates `i` from 1 to c (number of chords), and `j` from `i + 1` to c. `j` begins at `i + 1` in order to prevent double-counting intersections. This is a quadratic runtime complexity as for each chord, we compare it to every other chord (constant operations within 2 nested loops). This portion of the algorithm is `O(n^2)`.

The overall complexity of my `count_intersections` function is dominated by the nested loop structure for counting intersections, making it `O(n^2)`.


