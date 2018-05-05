# Sudoku Solver
 Sudoku is "**a denial of service attack on human intellect**". 
A puzzle is solved if the squares in each unit are filled with a permutation of the digits 1 to 9.
<pre><span class="pln"> A1 A2 A3</span><span class="pun">|</span><span class="pln"> A4 A5 A6</span><span class="pun">|</span><span class="pln"> A7 A8 A9 &nbsp; &nbsp;</span><span class="lit">4</span><span class="pln"> </span><span class="pun">.</span><span class="pln"> </span><span class="pun">.</span><span class="pln"> </span><span class="pun">|.</span><span class="pln"> </span><span class="pun">.</span><span class="pln"> </span><span class="pun">.</span><span class="pln"> </span><span class="pun">|</span><span class="lit">8</span><span class="pln"> </span><span class="pun">.</span><span class="pln"> </span><span class="lit">5</span><span class="pln"> &nbsp; &nbsp; </span><span class="lit">4</span><span class="pln"> </span><span class="lit">1</span><span class="pln"> </span><span class="lit">7</span><span class="pln"> </span><span class="pun">|</span><span class="lit">3</span><span class="pln"> </span><span class="lit">6</span><span class="pln"> </span><span class="lit">9</span><span class="pln"> </span><span class="pun">|</span><span class="lit">8</span><span class="pln"> </span><span class="lit">2</span><span class="pln"> </span><span class="lit">5</span><span class="pln"> <br>&nbsp;B1 B2 B3</span><span class="pun">|</span><span class="pln"> B4 B5 B6</span><span class="pun">|</span><span class="pln"> B7 B8 B9 &nbsp; &nbsp;</span><span class="pun">.</span><span class="pln"> </span><span class="lit">3</span><span class="pln"> </span><span class="pun">.</span><span class="pln"> </span><span class="pun">|.</span><span class="pln"> </span><span class="pun">.</span><span class="pln"> </span><span class="pun">.</span><span class="pln"> </span><span class="pun">|.</span><span class="pln"> </span><span class="pun">.</span><span class="pln"> </span><span class="pun">.</span><span class="pln"> &nbsp; &nbsp; </span><span class="lit">6</span><span class="pln"> </span><span class="lit">3</span><span class="pln"> </span><span class="lit">2</span><span class="pln"> </span><span class="pun">|</span><span class="lit">1</span><span class="pln"> </span><span class="lit">5</span><span class="pln"> </span><span class="lit">8</span><span class="pln"> </span><span class="pun">|</span><span class="lit">9</span><span class="pln"> </span><span class="lit">4</span><span class="pln"> </span><span class="lit">7</span><span class="pln"><br>&nbsp;C1 C2 C3</span><span class="pun">|</span><span class="pln"> C4 C5 C6</span><span class="pun">|</span><span class="pln"> C7 C8 C9 &nbsp; &nbsp;</span><span class="pun">.</span><span class="pln"> </span><span class="pun">.</span><span class="pln"> </span><span class="pun">.</span><span class="pln"> </span><span class="pun">|</span><span class="lit">7</span><span class="pln"> </span><span class="pun">.</span><span class="pln"> </span><span class="pun">.</span><span class="pln"> </span><span class="pun">|.</span><span class="pln"> </span><span class="pun">.</span><span class="pln"> </span><span class="pun">.</span><span class="pln"> &nbsp; &nbsp; </span><span class="lit">9</span><span class="pln"> </span><span class="lit">5</span><span class="pln"> </span><span class="lit">8</span><span class="pln"> </span><span class="pun">|</span><span class="lit">7</span><span class="pln"> </span><span class="lit">2</span><span class="pln"> </span><span class="lit">4</span><span class="pln"> </span><span class="pun">|</span><span class="lit">3</span><span class="pln"> </span><span class="lit">1</span><span class="pln"> </span><span class="lit">6</span><span class="pln"> <br></span><span class="pun">---------+---------+---------</span><span class="pln"> &nbsp; &nbsp;</span><span class="pun">------+------+------</span><span class="pln"> &nbsp; &nbsp;</span><span class="pun">------+------+------</span><span class="pln"><br>&nbsp;D1 D2 D3</span><span class="pun">|</span><span class="pln"> D4 D5 D6</span><span class="pun">|</span><span class="pln"> D7 D8 D9 &nbsp; &nbsp;</span><span class="pun">.</span><span class="pln"> </span><span class="lit">2</span><span class="pln"> </span><span class="pun">.</span><span class="pln"> </span><span class="pun">|.</span><span class="pln"> </span><span class="pun">.</span><span class="pln"> </span><span class="pun">.</span><span class="pln"> </span><span class="pun">|.</span><span class="pln"> </span><span class="lit">6</span><span class="pln"> </span><span class="pun">.</span><span class="pln"> &nbsp; &nbsp; </span><span class="lit">8</span><span class="pln"> </span><span class="lit">2</span><span class="pln"> </span><span class="lit">5</span><span class="pln"> </span><span class="pun">|</span><span class="lit">4</span><span class="pln"> </span><span class="lit">3</span><span class="pln"> </span><span class="lit">7</span><span class="pln"> </span><span class="pun">|</span><span class="lit">1</span><span class="pln"> </span><span class="lit">6</span><span class="pln"> </span><span class="lit">9</span><span class="pln"> <br>&nbsp;E1 E2 E3</span><span class="pun">|</span><span class="pln"> E4 E5 E6</span><span class="pun">|</span><span class="pln"> E7 E8 E9 &nbsp; &nbsp;</span><span class="pun">.</span><span class="pln"> </span><span class="pun">.</span><span class="pln"> </span><span class="pun">.</span><span class="pln"> </span><span class="pun">|.</span><span class="pln"> </span><span class="lit">8</span><span class="pln"> </span><span class="pun">.</span><span class="pln"> </span><span class="pun">|</span><span class="lit">4</span><span class="pln"> </span><span class="pun">.</span><span class="pln"> </span><span class="pun">.</span><span class="pln"> &nbsp; &nbsp; </span><span class="lit">7</span><span class="pln"> </span><span class="lit">9</span><span class="pln"> </span><span class="lit">1</span><span class="pln"> </span><span class="pun">|</span><span class="lit">5</span><span class="pln"> </span><span class="lit">8</span><span class="pln"> </span><span class="lit">6</span><span class="pln"> </span><span class="pun">|</span><span class="lit">4</span><span class="pln"> </span><span class="lit">3</span><span class="pln"> </span><span class="lit">2</span><span class="pln"> <br>&nbsp;F1 F2 F3</span><span class="pun">|</span><span class="pln"> F4 F5 F6</span><span class="pun">|</span><span class="pln"> F7 F8 F9 &nbsp; &nbsp;</span><span class="pun">.</span><span class="pln"> </span><span class="pun">.</span><span class="pln"> </span><span class="pun">.</span><span class="pln"> </span><span class="pun">|.</span><span class="pln"> </span><span class="lit">1</span><span class="pln"> </span><span class="pun">.</span><span class="pln"> </span><span class="pun">|.</span><span class="pln"> </span><span class="pun">.</span><span class="pln"> </span><span class="pun">.</span><span class="pln"> &nbsp; &nbsp; </span><span class="lit">3</span><span class="pln"> </span><span class="lit">4</span><span class="pln"> </span><span class="lit">6</span><span class="pln"> </span><span class="pun">|</span><span class="lit">9</span><span class="pln"> </span><span class="lit">1</span><span class="pln"> </span><span class="lit">2</span><span class="pln"> </span><span class="pun">|</span><span class="lit">7</span><span class="pln"> </span><span class="lit">5</span><span class="pln"> </span><span class="lit">8</span><span class="pln"> <br></span><span class="pun">---------+---------+---------</span><span class="pln"> &nbsp; &nbsp;</span><span class="pun">------+------+------</span><span class="pln"> &nbsp; &nbsp;</span><span class="pun">------+------+------</span><span class="pln"><br>&nbsp;G1 G2 G3</span><span class="pun">|</span><span class="pln"> G4 G5 G6</span><span class="pun">|</span><span class="pln"> G7 G8 G9 &nbsp; &nbsp;</span><span class="pun">.</span><span class="pln"> </span><span class="pun">.</span><span class="pln"> </span><span class="pun">.</span><span class="pln"> </span><span class="pun">|</span><span class="lit">6</span><span class="pln"> </span><span class="pun">.</span><span class="pln"> </span><span class="lit">3</span><span class="pln"> </span><span class="pun">|.</span><span class="pln"> </span><span class="lit">7</span><span class="pln"> </span><span class="pun">.</span><span class="pln"> &nbsp; &nbsp; </span><span class="lit">2</span><span class="pln"> </span><span class="lit">8</span><span class="pln"> </span><span class="lit">9</span><span class="pln"> </span><span class="pun">|</span><span class="lit">6</span><span class="pln"> </span><span class="lit">4</span><span class="pln"> </span><span class="lit">3</span><span class="pln"> </span><span class="pun">|</span><span class="lit">5</span><span class="pln"> </span><span class="lit">7</span><span class="pln"> </span><span class="lit">1</span><span class="pln"> <br>&nbsp;H1 H2 H3</span><span class="pun">|</span><span class="pln"> H4 H5 H6</span><span class="pun">|</span><span class="pln"> H7 H8 H9 &nbsp; &nbsp;</span><span class="lit">5</span><span class="pln"> </span><span class="pun">.</span><span class="pln"> </span><span class="pun">.</span><span class="pln"> </span><span class="pun">|</span><span class="lit">2</span><span class="pln"> </span><span class="pun">.</span><span class="pln"> </span><span class="pun">.</span><span class="pln"> </span><span class="pun">|.</span><span class="pln"> </span><span class="pun">.</span><span class="pln"> </span><span class="pun">.</span><span class="pln"> &nbsp; &nbsp; </span><span class="lit">5</span><span class="pln"> </span><span class="lit">7</span><span class="pln"> </span><span class="lit">3</span><span class="pln"> </span><span class="pun">|</span><span class="lit">2</span><span class="pln"> </span><span class="lit">9</span><span class="pln"> </span><span class="lit">1</span><span class="pln"> </span><span class="pun">|</span><span class="lit">6</span><span class="pln"> </span><span class="lit">8</span><span class="pln"> </span><span class="lit">4</span><span class="pln"> <br>&nbsp;I1 I2 I3</span><span class="pun">|</span><span class="pln"> I4 I5 I6</span><span class="pun">|</span><span class="pln"> I7 I8 I9 &nbsp; &nbsp;</span><span class="lit">1</span><span class="pln"> </span><span class="pun">.</span><span class="pln"> </span><span class="lit">4</span><span class="pln"> </span><span class="pun">|.</span><span class="pln"> </span><span class="pun">.</span><span class="pln"> </span><span class="pun">.</span><span class="pln"> </span><span class="pun">|.</span><span class="pln"> </span><span class="pun">.</span><span class="pln"> </span><span class="pun">.</span><span class="pln"> &nbsp; &nbsp; </span><span class="lit">1</span><span class="pln"> </span><span class="lit">6</span><span class="pln"> </span><span class="lit">4</span><span class="pln"> </span><span class="pun">|</span><span class="lit">8</span><span class="pln"> </span><span class="lit">7</span><span class="pln"> </span><span class="lit">5</span><span class="pln"> </span><span class="pun">|</span><span class="lit">2</span><span class="pln"> </span><span class="lit">9</span><span class="pln"> </span><span class="lit">3</span><span class="pln"> </span></pre>

- row - r
- column - c
- square - s
- digit - d
- unit - u, ['A1','B1','C1','D1','E1','F1','G1','H1','I1']
- grid - grid, 81 non-blank chars, starting with '.18...7...
- values - dict of possible values, {'A1':'12349', 'A2':'8', ...}

## Datasets
Easy dataset : dataset1.txt

Normal dataset : dataset2.txt

Hard dataset : dataset3.txt (**Arto Inkala**'s puzzle)
