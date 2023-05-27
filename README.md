# Emergency_Call_Transcriber

## Transcribing an Emergency Call

### Overview

The aim of this project is to develop a system that improves the efficiency of emergency response teams by accurately transcribing names from emergency calls and matching them with the corresponding individual's information in the DMV (Department of Motor Vehicles) database. The system will address issues such as misheard names, mistyped names, and arbitrary misspellings to ensure faster and more accurate search results, allowing the emergency response team to quickly identify and locate the person in need.

### Features and Functionality

**1. Perfect Name Matching:** The system will start by performing a direct match between the transcribed names and the names in the DMV database. If a perfect match is found, the system will retrieve the corresponding address from the database.

**2. Misspelling Detection and Correction:** To handle cases where the transcribed names have basic misspellings, the system will utilize string edit distance algorithms. By calculating the similarity between the transcribed name and the names in the database, the system can detect and correct simple misspellings. For example, if "Shelvy Silvester" is transcribed instead of "Shelby Sylvester," the system can identify the missing and incorrect letters and provide the correct match.

**3. Metaphone Matching:** The system will tackle more complex misspellings and variations in the transcribed names using metaphone matching. Metaphone is a phonetic algorithm that converts words into phonetic representations, allowing for approximate matching of similar-sounding names. The system will generate metaphone codes for both the transcribed names and the names in the DMV database, and then compare these codes to identify potential matches. This approach will handle cases where transcribers use different spellings for similar-sounding names.

### Responding to Calls

- **The Basics**
First step: making sure that if the name is transcribed perfectly, we match that person's record in the database right away. An example is below.

    **Input**

    ```bash
    3
    Courtney Mackstutis
    Angela Gimbel
    Hector Koba
    з
    Courtney Mackstutis;4766 Moctezuma
    Angela Gimbel;1270 Finazzo
    Hector Koba;7074 Turrill
    ```

    **Output**

    ```bash
    ["4766 Moctezuma", "1270 Finazzo", "7074 Turrill"]
    ```

- **Misspellings**
The second thing to look for are basic misspellings due to the transcriber hearing the name correctly but missing a keystroke or pressing the wrong key instead. Think "Shelby Sylvester" turns into "Shelvy Silvester" or "Ginette Carlock" turns into "Ginete Carlock". In the first example, the transcriber missed the "b" key and hit "v" instead, and missed "y" and hit "¡" instead. In the second, the transcriber accidentally missed a letter in the first name and added an additional one in the last name.

    **Input**

    ```bash
    3
    Courtnet Mackstutis
    Angela Gimbrel
    Hector Kba
    3
    Courtney Mackstutis; 4766 Moctezuma
    Angela Gimbel;1270 Finazzo
    Hector Koba;7074 Turrill
    ```

    **Output**

    ```bash
    ["4766 Moctezuma", "1270 Finazzo", "7074 Turrill"]
    ```

- **Metaphones**
The last and trickiest instance of transcription comes in the form of arbitrary misspellings resulting from the transcriber either hearing the name correctly and using a different spelling than the one in our database, or mishearing the name in some form.
Think "Ashley" vs. "Ashlee" vs. "Ashleigh" or "Henry David Thoreau" turns into "Henney David Surrow".

    **Input**

    ```bash
    3
    Kourtnie Makstuttis
    Anjelica Gimbell
    Hector Cobrah
    Courtney Mackstutis; 4766 Moctezuma
    Angela Gimbel; 1270 Finazzo
    Hector Koba; 7074 Turrill
    ```

    **Output**

    ```bash
    ["4766 Moctezuma", "1270 Finazzo", "7074 Turrill"]
    ```


<!-- #### Input
```
Download
3
Ashley Johnson
Cheryl Xiao
Henry Thoreau
6
Ashley Thompson;9295 Heiler
Ashleigh Jonson;9877 Talsma
Cheryl Xist;6232 Schnarr
Sheryl Shao;9824 Tyrol
Henry Thireat;8692 Anzualda
Henry Surrow;7542 Lunden
``` -->
<!-- 
#### Your Output
```
9295 Heiler
6232 Schnarr
8692 Anzualda
``` -->

<!-- #### Expected Output
```
9877 Talsma
9824 Tyrol
7542 Lunden
``` -->

