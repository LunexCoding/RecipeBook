# Goals

1. Build the first full-featured application to easily interact with recipes on a PC.
2. Get real development experience.

# Objectives

1. [x] Add a file system module.


2. [x] Create a `RecipeBook` package consisting of modules:
   1. [x] `ingredient`
   2. [x] `recipe`
   3. [x] `book`


3. [x] Add storages:
   1. [x] `storage.py` - to store information about products in stock
   2. [x] `ingredientsDB.py` - base for operations with products in memory


4. [x] Add logging:
   1. [x] Write log to `md` file.
   2. [x] Separate log for testing.


5. [x] Saving data:
   1. [x] Local file system:
      1. [x] recipe data - json format:
          ```json
          {
              "_name": ...,
              "_ingredients": [
                  {
                      "_name": ...,
                      "_measure": ...
                  },
                  ...
              ],
              "_cookingSteps": {
                  "id": ...,
                  ...
              },
              "_description": ...,
              "_isFavorite": ...
          }
          ```
      2. [x] storage data - json format:
           ```json
           {
              "productID": ...,
              ...
           }
           ```

      3. [x] ingredientsDB data - json format:
           ```json
           {
              "1": {
                  "_name": ...,
                  "_measure": ...
              },
              ...
           }
           ```
   2. [ ] FTP:
      1. [ ] Upload files to FTP
      2. [ ] Download files from FTP
      3. [ ] Checking the relevance of data on FTP


6. [ ] Add filtering/sorting by:
   1. [ ] Name
   2. [ ] Rating
   3. [ ] Favorite
   4. [ ] Available for cooking


7. [ ] GUI:
   1. [x] Basic interface
   2. [ ] Element Grid
   3. [ ] Filling with information


8. [ ] Testing:
   1. [ ] basic (Available only after writing a console prototype)
   2. [ ] GUI
   3. [ ] FTP
   4. [ ] Integration with Telegram


9. [ ] Integration with Telegram:
    1. [ ] Authorization
    2. [ ] Sending a shopping list message

# Note

> The project will receive a zero version (will be released) when it reaches the development mark of ***60%***.