#!/usr/bin/python

import pytest
import sys
import classes.search as bs

def test_book_search_isbn():
    query = bs.Search({'isbn':'9780470135006'})
    assert bs.Search.searchByQuery(query) == { "body": { "books": [{ "author": ["Bobrow Test Preparation Services"], "isbn": "9780470135006", "publication_date": 2008, "publisher": "Cliffs Notes", "title": "CliffsAP Chemistry (Cliffsap)" }] }, "headers": { "Content-Type": "application/json" }, "statusCode": 200 }

def test_book_search_author():
    query = bs.Search({'query':'Phillip%20Laplante'})
    assert bs.Search.searchByQuery(query) == { "body": { "books": [ { "author": [ "Phillip Laplante" ], "isbn": "9780830639526", "publication_date": 1992, "publisher": "Windcrest", "title": "Easy PC maintenance and repair" }, { "author": [ "Phillip Laplante" ], "isbn": "0780347315", "publication_date": 1999, "publisher": "Institute of Electrical & Electronics Enginee", "title": "Electrical Engineering Dictionary" }, { "author": [ "Phillip Laplante" ], "isbn": "9780849326974", "publication_date": 2000, "publisher": "Crc Pr I Llc", "title": "Dictionary of Computer Science, Engineering, and Technology" }, { "author": [ "Phillip Laplante" ], "isbn": "0780323394", "publication_date": 1997, "publisher": "Institute of Electrical & Electronics Enginee", "title": "Design and Application of Real-Time Systems" }, { "author": [ "Phillip A. Laplante" ], "isbn": "9780780311527", "publication_date": 1993, "publisher": "IEEE Computer Society Press", "title": "Real-Time Systems Design and Analysis" }, { "author": [ "Phillip A. Laplante" ], "isbn": "0849313767", "publication_date": 2003, "publisher": "Taylor and Francis", "title": "Software engineering for image processing systems" }, { "author": [ "Phillip A. Laplante" ], "isbn": "0849372283", "publication_date": 2007, "publisher": "Taylor and Francis", "title": "What every engineer should know about software engineering" }, { "author": [ "Phillip A. Laplante" ], "isbn": "9780830639526", "publication_date": 1992, "publisher": "Windcrest/McGraw-Hill", "title": "Easy PC maintenance and repair" }, { "author": [ "Phillip A. Laplante" ], "isbn": "1420031244", "publication_date": 2005, "publisher": "Taylor and Francis", "title": "AntiPatterns" }, { "author": [ "Phillip A. Laplante" ], "isbn": "0780353412", "publication_date": 2001, "publisher": "Institute of Electrical & Electronics Enginee", "title": "Real-Time Systems" }, { "author": [ "Phillip A. Laplante" ], "isbn": "9781420064674", "publication_date": 2009, "publisher": "Auerbach Publications", "title": "Requirements engineering for software and systems" }, { "author": [ "Phillip A. Laplante" ], "isbn": "0780368169", "publication_date": 1996, "publisher": "Institute of Electrical & Electronics Enginee", "title": "Design and Application of Real-Time Systems" }, { "author": [ "Phillip A. Laplante" ], "isbn": "9780780348028", "publication_date": 1999, "publisher": "Institute of Electrical & Electronics Enginee", "title": "Successful Software Project Management" }, { "author": [ "Phillip A. Laplante" ], "isbn": "0830644342", "publication_date": 1993, "publisher": "Windcrest/McGraw Hill", "title": "Fractal mania" }, { "author": [ "Phillip A. Laplante" ], "isbn": "9780780348387", "publication_date": 2001, "publisher": "Inst Elect & Electronic Engineers", "title": "Software Engineering Ssc" }, { "author": [ "Phillip A. Laplante" ], "isbn": "1590338898", "publication_date": 2003, "publisher": "Nova Science Publishers", "title": "Biocomputing" }, { "author": [ "Phillip Laplante", "Thomas Costello" ], "isbn": "0131855891", "publication_date": 2005, "publisher": "Prentice Hall PTR", "title": "CIO Wisdom II" }, { "author": [ "Phillip Laplante", "Thomas Costello" ], "isbn": "0131855891", "publication_date": 2005, "publisher": "Prentice Hall PTR", "title": "CIO Wisdom II" }, { "author": [ "Phillip A. Laplante" ], "isbn": "9781439820858", "publication_date": 2011, "publisher": "CRC Press", "title": "Technical Writing A Practical Guide For Engineers And Scientists" }, { "author": [ "Phillip A. Laplante" ], "isbn": "9780849326912", "publication_date": 2001, "publisher": "CRC Press", "title": "Dictionary of computer science, engineering, and technology" }, { "author": [ "Phillip A. Laplante" ], "isbn": "0314012621", "publication_date": 1993, "publisher": "West Pub. Co.", "title": "Using UNIX" }, { "author": [ "Phillip A. Laplante" ], "isbn": "0849330866", "publication_date": 2005, "publisher": "Taylor & Francis Books Ltd/CRC", "title": "Comprehensive dictionary of electrical engineering" }, { "author": [ "Phillip A. Laplante" ], "isbn": "0849331285", "publication_date": 1999, "publisher": "CRC Press", "title": "Comprehensive dictionary of electrical engineering" }, { "author": [ "Phillip A. Laplante" ], "isbn": "9780780348035", "publication_date": 1999, "publisher": "Institute of Electrical & Electronics Enginee", "title": "Keys to Successful Software Development" }, { "author": [ "Phillip A. Laplante" ], "isbn": "9780780348158", "publication_date": 1999, "publisher": "Institute of Electrical & Electronics Enginee", "title": "A Practical Approach to Real-Time Systems" }, { "author": [ "Phillip A. Laplante" ], "isbn": "0471228559", "publication_date": 2004, "publisher": "Wiley", "title": "Real-time system design and analysis" }, { "author": [ "Philip A. Laplante", "Phillip A. Laplante" ], "isbn": "9780780334007", "publication_date": 1996, "publisher": "John Wiley & Sons", "title": "Real-Time Systems Design and Analysis" }, { "author": [ "Philip A. Laplante", "Phillip A. Laplante" ], "isbn": "9781420059779", "publication_date": 2010, "publisher": "AUERBACH", "title": "Encyclopedia of Software Engineering, Three Volume Set" }, { "author": [ "Nasser Kehtarnavaz", "Phillip A. Laplante" ], "isbn": "0819456446", "publication_date": 2005, "publisher": "IS&T", "title": "Real-time imaging IX" }, { "author": [ "Nasser Kehtarnavaz", "Phillip A. Laplante" ], "isbn": "9780819448125", "publication_date": 2003, "publisher": "SPIE", "title": "Real-time imaging VII" }, { "author": [ "Nasser Kehtarnavaz", "Phillip A. Laplante" ], "isbn": "9780819461032", "publication_date": 2006, "publisher": "IS&T", "title": "Real-time image processing 2006" }, { "author": [ "William F. Gilreath", "Phillip A. Laplante" ], "isbn": "1402074166", "publication_date": 2003, "publisher": "Springer", "title": "Computer Architecture" }, { "author": [ "Phillip A. Laplante", "Alexander D. Stoyenko" ], "isbn": "0780310683", "publication_date": 1996, "publisher": "IEEE Press", "title": "Real-time imaging" }, { "author": [ "Phillip A. Laplante", "Wolfgang A. Halang" ], "isbn": "9780080425900", "publication_date": 1996, "publisher": "Pergamon", "title": "Real time programming 1995" }, { "author": [ "C. B. Johnson", "Divyendu Sinha", "Phillip A. Laplante" ], "isbn": "0819445630", "publication_date": 2003, "publisher": "SPIE", "title": "Low-light-level and real-time imaging systems, components, and applications" }, { "author": [ "Phillip A. Laplante", "Alexander D. Stoyenko", "Divyendu Sinha" ], "isbn": "0819420352", "publication_date": 1996, "publisher": "SPIE", "title": "Real-time imaging" }, { "author": [ "William F. Gilreath" ], "isbn": "1402074166", "publication_date": 2003, "publisher": "Kluwer Academic Publishers", "title": "Computer architecture" }, { "author": [ "Edward R. Dougherty" ], "isbn": "9780819417893", "publication_date": 1995, "publisher": "SPIE Optical Engineering Press", "title": "Introduction to real-time imaging" }, { "author": [ "William F. Gilreath" ], "isbn": "146134980X", "publication_date": 2003, "publisher": "Springer US", "title": "Computer Architecture: A Minimalist Perspective" }, { "author": [ "Bad author - no name" ], "isbn": "9780819448125", "publication_date": 2003, "publisher": "SPIE", "title": "Real-time imaging VII" }, { "author": [ "Colin J. Neill" ], "isbn": "1439861862", "publication_date": 2011, "publisher": "Auerbach Publications", "title": "Antipatterns" } ] }, "headers": { "Content-Type": "application/json" }, "statusCode": 200 }

def test_book_search_no_params():
    query = bs.Search({'test':'test'})
    assert bs.Search.searchByQuery(query) == { "body": { "error": "Please provide search parameter" }, "headers": { "Content-Type": "application/json" }, "statusCode": 404 }

def test_book_search_title():
    query = bs.Search({'query':'Child%20Called%20It'})
    assert bs.Search.searchByQuery(query) == { "body": { "books": [{ "author": ["David J. Pelzer"], "isbn": "9780929099026", "publication_date": 1987, "publisher": "Planeta", "title": "A child called \"it\"" }, { "author": ["David J. Pelzer"], "isbn": "075284170X", "publication_date": 2002, "publisher": "Orion (an Imprint of The Orion Publishing Group Ltd )", "title": "A child called \"It\"" }, { "author": ["David J. Pelzer"], "isbn": "0739400614", "publication_date": 1995, "publisher": "Health Communications", "title": "A Child called \"it\"" }, { "author": ["David J. Pelzer"], "isbn": "9789796864003", "publication_date": 2003, "publisher": "Gramedia Pustaka Utama", "title": "A child called 'It'" }, { "author": ["William Shakespeare"], "isbn": "075405084X", "publication_date": 1788, "publisher": "Book Jungle", "title": "Hamlet" }, { "author": ["David J. Pelzer"], "isbn": "0739400614", "publication_date": 1995, "publisher": "Health Communications", "title": "A Child called \"it\" and The lost boy" }, { "author": ["Louise Armstrong"], "isbn": "9780201626926", "publication_date": 1993, "publisher": "Addison-Wesley", "title": "And They Call It Help" }, { "author": ["Church of England"], "isbn": "066514637X", "publication_date": 1788, "publisher": "C.J. Thynne", "title": "Book of common prayer" }, { "author": ["Dave Pelzer"], "isbn": "0795345577", "publication_date": 2015, "publisher": "RosettaBooks", "title": "Too Close to Me: The Middle-Aged Consequences of Revealing a Child Called It" }, { "author": ["Penelope Leach"], "isbn": "9780394552750", "publication_date": 1986, "publisher": "Knopf", "title": "Your Growing Child" }, { "author": ["William Morris"], "isbn": "9781425070335", "publication_date": 2006, "publisher": "Dodo Press", "title": "Child Christopher and Goldilind the Fair" }, { "author": ["Debra Brady"], "isbn": "9780312281762", "publication_date": 2003, "publisher": "St. Martin's Griffin", "title": "How to Save Your Child's Life" }, { "author": ["World Health Organization"], "isbn": "9241562218", "publication_date": 2003, "publisher": "World Health Organization", "title": "Global Strategy for Infant and Young Child Feeding" }, { "author": ["John Milton"], "isbn": "9780849207266", "publication_date": 1919, "publisher": "printed for the proprietors, by Bunney and Gold", "title": "Comus" }, { "author": ["C. S. Lewis"], "isbn": "1435117158", "publication_date": 1990, "publisher": "Caedmon", "title": "The Chronicles of Narnia" }, { "author": ["Stephen King"], "isbn": "9780937986905", "publication_date": 1991, "publisher": "Plume", "title": "The Drawing of the Three" }, { "author": ["Stephen King"], "isbn": "0450054799", "publication_date": 1986, "publisher": "ISIS Large Print", "title": "Night Shift" }, { "author": ["Henry Adams"], "isbn": "0891908447", "publication_date": 1986, "publisher": "Digireads.com", "title": "The Education of Henry Adams" }, { "author": ["Kosuke Fujishima"], "isbn": "9781569719503", "publication_date": 1996, "publisher": "Dark Horse", "title": "Oh My Goddess!" }, { "author": ["David J. Pelzer"], "isbn": "0757301673", "publication_date": 2003, "publisher": "Health Communications, Inc.", "title": "The lost boy" }, { "author": ["Henry James, Jr."], "isbn": "9781425017033", "publication_date": 2006, "publisher": "ReadHowYouWant.com", "title": "The Point of View" }, { "author": ["Guy de Maupassant"], "isbn": "1417999691", "publication_date": 2004, "publisher": "Kessinger Publishing", "title": "Original Maupassant Short Stories" }, { "author": ["Jonathan Kellerman"], "isbn": "9780345521484", "publication_date": 1987, "publisher": "Ballantine Books", "title": "Over the edge" }, { "author": ["David J. Pelzer"], "isbn": "9780752852720", "publication_date": 2002, "publisher": "Orion", "title": "My story" }, { "author": ["Lois Lowry"], "isbn": "9780385734165", "publication_date": 2008, "publisher": "Yearling", "title": "Gossamer" }, { "author": ["Stanley I. Greenspan"], "isbn": "9780140077230", "publication_date": 1986, "publisher": "Viking", "title": "First feelings" }, { "author": ["S P. Somtow"], "isbn": "9780061059933", "publication_date": 2000, "publisher": "HarperEntertainment", "title": "Crow" }, { "author": ["Sharon M. Draper"], "isbn": "9780689818516", "publication_date": 1998, "publisher": "Atheneum Books for Young Readers", "title": "Forged by fire" }, { "author": ["Mic Hunter"], "isbn": "9780669208665", "publication_date": 1991, "publisher": "Ballantine Books", "title": "Abused boys" }, { "author": ["Natasha T. Hays"], "isbn": "1843107880", "publication_date": 2003, "publisher": "Jessica Kingsley Publishers", "title": "A Toss of the Dice" }, { "author": ["Nurul Islam"], "isbn": "1560223014", "publication_date": 2006, "publisher": "Food Products Press", "title": "Reducing Rural Poverty in Asia" }, { "author": ["Deanne A. Crone", "Robert H. Horner", "Leanne S. Hawken"], "isbn": "9781572309401", "publication_date": 2003, "publisher": "The Guilford Press", "title": "Responding to Problem Behavior in Schools" }, { "author": ["Tasmin Jahan"], "isbn": "190671018X", "publication_date": 2009, "publisher": "Pen Press", "title": "Stinging Filth and Bloody Hands" }, { "author": ["Peter Charleton"], "isbn": "9781842181010", "publication_date": 2006, "publisher": "Blackhall", "title": "Lies In a Mirror" }] }, "headers": { "Content-Type": "application/json" }, "statusCode": 200 }