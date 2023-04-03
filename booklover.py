{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd \n",
    "\n",
    "import unittest \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [],
   "source": [
    "# this is for Task 1 of HW08 - create a class in file named booklover.py. I start with method 1 and then move to \n",
    "# method 2 and method 3 and method 4. \n",
    "#**Method 1:**\n",
    "\n",
    "#`add_book(book_name, rating)`:\n",
    "#- This function takes a `book name` (string) and `rating` (integer from 0 to 5)\n",
    "#- It tries to add the book to `book_list`. See hint below on how to pass a new book to the dataframe.\n",
    "#- Only add a book to the person’s `book_list` if that book doesn’t already exist.\n",
    "#  - It is sufficient to match on `book_name`.\n",
    "#- If it does exist, tell the user.\n",
    "\n",
    "#Hint: To add a new book to the book list (which is a dataframe), do this in your method, where `book_name` and `book_rating` are the arguments passed to the method.:\n",
    "\n",
    "#```python\n",
    "#new_book = pd.DataFrame({\n",
    "#    'book_name': [book_name], \n",
    "#    'book_rating': [book_rating]\n",
    "#})\n",
    "#self.book_list = pd.concat([self.book_list, new_book], ignore_index=True)\n",
    "#```\n",
    "\n",
    "#Of course, be sure to see if `book_name` is not in the book list.\n",
    "\n",
    "class BookLover:\n",
    "    \n",
    "    def __init__(self, name, email, fav_genre, num_books=0, book_list=pd.DataFrame({'book_name':[], 'book_rating':[]})):\n",
    "\n",
    "        self.name = name\n",
    "        self.email = email\n",
    "        self.fav_genre = fav_genre\n",
    "        self.num_books = num_books\n",
    "        self.book_list = book_list\n",
    "    \n",
    "    def add_book(self, book_name, rating):\n",
    "        \n",
    "        if book_name not in self.book_list['book_name'].values:\n",
    "            new_book = pd.DataFrame({\n",
    "                'book_name': [book_name], \n",
    "                'book_rating': [rating]\n",
    "            })\n",
    "            self.book_list = pd.concat([self.book_list, new_book], ignore_index=True)\n",
    "            self.num_books += 1\n",
    "        else:\n",
    "            print(f\"{self.name} was previously read {book_name}.\")\n",
    "    \n",
    "# **Method 2:**\n",
    "\n",
    "#`has_read(book_name)`\n",
    "#- This function takes `book_name` (string) as input and determines if the person has read the book.\n",
    "#  - That is, if that `book name` is in `book_list`. \n",
    "#  - Again, it is sufficient to match on `book_name`.\n",
    "#- The method should return `True` if the person has read the book, `False` otherwise.   \n",
    "    \n",
    "    \n",
    "    \n",
    "    def has_read(self, book_name):\n",
    "        \n",
    "        if book_name in self.book_list['book_name'].values:\n",
    "            return True\n",
    "        else:\n",
    "            return False\n",
    "#**Method 3:**\n",
    "\n",
    "#`num_books_read()`\n",
    "#- This function takes no parameters and just returns the total number of books the person has read. \n",
    "\n",
    "    def num_books_read(self):\n",
    "        \n",
    "        return self.num_books\n",
    "\n",
    "#**Method 4:**\n",
    "\n",
    "#`fav_books()`:\n",
    "#- This function takes no parameters and returns the filtered dataframe of the person’s most favorite books. \n",
    "#- Books in this list should have a rating > 3.  \n",
    "\n",
    "    def fav_books(self):\n",
    "        \n",
    "        return self.book_list[self.book_list['book_rating'] > 3]\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "True\n",
      "5\n",
      "           book_name  book_rating\n",
      "0  War of the Worlds          4.0\n",
      "2  The Divine Comedy          5.0\n",
      "3      The Popol Vuh          5.0\n",
      "4      The Outsiders          4.0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "<ipython-input-7-c227f53af539>:36: FutureWarning: elementwise comparison failed; returning scalar instead, but in the future will perform elementwise comparison\n",
      "  if book_name not in self.book_list['book_name'].values:\n"
     ]
    }
   ],
   "source": [
    "#Testing\n",
    "#A final option -- which the test file will use -- is to put this code at the bottom of your `.py` file, after and outside of your class definition:\n",
    "\n",
    "#```python\n",
    "\n",
    "#if __name__ == '__main__':\n",
    "    \n",
    " #   test_object = BookLover(\"Han Solo\", \"hsolo@millenniumfalcon.com\", \"scifi\")\n",
    "  #  test_object.add_book(\"War of the Worlds\", 4)\n",
    "    # And so forth\n",
    "\n",
    "#```\n",
    "\n",
    "#NOTE: The methods listed above do not have `self` as their first argument, but they should in your class.\n",
    "    \n",
    "if __name__ == '__main__':\n",
    "    \n",
    "    test_object = BookLover(\"Han Solo\", \"hsolo@millenniumfalcon.com\", \"scifi\")\n",
    "    test_object.add_book(\"War of the Worlds\", 4)\n",
    "    test_object.add_book(\"Fight Club\", 3)\n",
    "    test_object.add_book(\"The Divine Comedy\", 5)\n",
    "    test_object.add_book(\"The Popol Vuh\", 5)\n",
    "    test_object.add_book(\"The Outsiders\", 4)\n",
    "    print(test_object.has_read(\"The Divine Comedy\"))\n",
    "    print(test_object.num_books_read())\n",
    "    print(test_object.fav_books())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
