# Emergency_Call_Transcriber

## Transcribing an Emergency Call

### Problem Statement

#### Introduction

Imagine you are working with an emergency response team to respond to 911 calls as quickly as possible. One of the biggest problems the team faces is handling the transcription of the names of callers. You've noticed that sometimes the name is misheard by the person taking the call, sometimes it is simply mistyped, and sometimes both. These problems make it more difficult to search the database of DMV records to identify and locate the individual in need.

You would like to help solve this problem, and ensure the fastest response rates possible to help those in need. You have read and write access to the list of transcribed names and the database of DMV records. We need a way to effectively translate names based on their transcriptions and be able to narrow our search results to the one individual whose location we are interested in.

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

