{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'null' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[0;32m<ipython-input-3-f2decc16b180>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[1;32m      4\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      5\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0munittest\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 6\u001b[0;31m \u001b[0;32mfrom\u001b[0m \u001b[0mbooklover\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mBookLover\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      7\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      8\u001b[0m \u001b[0;32mclass\u001b[0m \u001b[0mBookLoverTestSuite\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0munittest\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mTestCase\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m/sfs/qumulo/qhome/fvc7fe/Documents/MSDS/DS5100/DS5100-2023-01-O/lessons/booklover.py\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[1;32m    159\u001b[0m   {\n\u001b[1;32m    160\u001b[0m    \u001b[0;34m\"cell_type\"\u001b[0m\u001b[0;34m:\u001b[0m \u001b[0;34m\"code\"\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 161\u001b[0;31m    \u001b[0;34m\"execution_count\"\u001b[0m\u001b[0;34m:\u001b[0m \u001b[0mnull\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    162\u001b[0m    \u001b[0;34m\"metadata\"\u001b[0m\u001b[0;34m:\u001b[0m \u001b[0;34m{\u001b[0m\u001b[0;34m}\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    163\u001b[0m    \u001b[0;34m\"outputs\"\u001b[0m\u001b[0;34m:\u001b[0m \u001b[0;34m[\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;31mNameError\u001b[0m: name 'null' is not defined"
     ]
    }
   ],
   "source": [
    "#Create a test suite for the previous class in a file named `booklover_test.py`.\n",
    "#In the file, write a class called `BookLoverTestSuite`, being sure to import the `unittest` library \n",
    "#and the BookLover class from the first file.\n",
    "\n",
    "import unittest\n",
    "from booklover import BookLover\n",
    "\n",
    "class BookLoverTestSuite(unittest.TestCase):\n",
    "    \n",
    "#    - `test_1_add_book()`: Add a book and test if it is in `book_list`.\n",
    "\n",
    "    def test_1_add_book(self):\n",
    "        bookl = BookLover()\n",
    "        bookl.add_book(\"The Terminal List\")\n",
    "        self.assertIn(\"The Terminal List\", bookl.book_list)\n",
    "        \n",
    "# `test_2_add_book()`: Add the same book twice. Test if it's in `book_list` only once.  \n",
    "\n",
    "    def test_2_add_book(self):\n",
    "        bookl = BookLover()\n",
    "        bookl.add_book(\"Travels with Charley\")\n",
    "        bookl.add_book(\"Travels with Charley\")\n",
    "        self.assertEqual(1, bookl.num_books())\n",
    "\n",
    "#- `test_3_has_read()`: Pass a book in the list and test the answer is `True`.        \n",
    "        \n",
    "    def test_3_has_read(self):\n",
    "        bookl = BookLover()\n",
    "        bookl.add_book(\"The Outsiders\")\n",
    "        bookl.mark_book_as_read(\"The Outsiders\")\n",
    "        self.assertTrue(bookl.has_read(\"The Outsiders\"))\n",
    "\n",
    "#- `test_4_has_read()`: Pass a book NOT in the list and use `assert False` to test if the answer is `True`\n",
    "\n",
    "    def test_4_has_read(self):\n",
    "        bookl = BookLover()\n",
    "        self.assertFalse(bookl.has_read(\"Atlas Shrugged\"))\n",
    "\n",
    "#- `test_5_num_books_read()`: Add some books to the list, and test num_books matches expected.\n",
    "        \n",
    "    def test_5_num_books_read(self):\n",
    "        bookl = BookLover()\n",
    "        bookl.add_book(\"The Odyssey\")\n",
    "        bookl.add_book(\"Lonesome Dove\")\n",
    "        bookl.mark_book_as_read(\"Lonesome Dove\")\n",
    "        self.assertEqual(1, bookl.num_books_read())\n",
    "        \n",
    "#- `test_6_fav_books()`: Add some books with ratings to the list, making sure some of them have rating > 3. \n",
    "        \n",
    "    def test_6_fav_books(self):\n",
    "        bookl = BookLover()\n",
    "        bookl.add_book_with_rating(\"Enders Game\", 4)\n",
    "        bookl.add_book_with_rating(\"Outliers\", 4)\n",
    "        bookl.add_book_with_rating(\"Lord of the Rings\", 5)\n",
    "        fav_books = bookl.get_favorite_books()\n",
    "        for book in fav_books:\n",
    "            self.assertGreater(book[1], 3)\n",
    "                \n",
    "if __name__ == '__main__':\n",
    "    unittest.main(verbosity=3)"
   ]
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
