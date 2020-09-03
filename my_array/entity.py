class GameEntry:

    def __init__(self, name, score):
        self._name = name
        self._score = score

    def get_name(self):
        return self._name

    def get_score(self):
        return self._score

    def __str__(self):
        return '({0},{1})'.format(self._name, self._score)


class Scoreboard:
    def __init__(self, capacity=10):
        self._board = [None] * capacity
        self._n = 0

    def __getitem__(self, item):
        return self._board[item]

    def __str__(self):
        return '\n'.join(str(self._board[j] for j in range(self._n)))

    def add(self, entry):
        # assert entry isinstance(GameEntry)

        score = entry.get_score()
        good = self._n < len(self._board) or score > self._board[-1].get_score()
        if good:
            if self._n < len(self._board):
                self._n += 1
            j = self._n - 1
            while j > 0 and self._board[j - 1].get_score() < score:
                self._board[j] = self._board[j - 1]
                j -= 1
            self._board[j] = entry


def _transform(original, code):
    msg = list(original)
    for k in range(len(msg)):
        if msg[k].isupper():
            j = ord(msg[k]) - ord('A')
            msg[k] = code[j]
    return ''.join(msg)


class CaesarCipher:
    def __init__(self, shift):
        encoder = [None] * 26
        decoder = [None] * 26
        for k in range(26):
            encoder[k] = chr((k + shift) % 26 + ord('A'))
            decoder[k] = chr((k - shift) % 26 + ord('A'))
        self._forward = ''.join(encoder)
        self._backward = ''.join(decoder)

    def encrypt(self, message):
        return _transform(message, self._forward)

    def decrypt(self, secret):
        return _transform(secret, self._backward)


class TicTacToe:
    def __init__(self):
        self._board = [[' '] *3 for j in range(3)]
        self._player = 'X'

    def mark(self, i, j):
        if not (0 <=i<=2 and 0<=j<=2):
            raise ValueError("invalid board position")
        if self._board[i][j] != ' ':
            raise ValueError('Board position occupid')
        if self.winner() is not None:
            raise ValueError('Game is already complete')
        self._board[i][j] = self._player
        if self._player == 'X':
            self._board = 'O'
        else:
            self._player = 'X'


    def _is_win(self, mark):
        board = self._board
        return (mark)

    def winner(self):
        for mark in 'XO':
            if self._is_win(mark):
                return mark
        return None

    def __str__(self):
        rows = ['|'.join(self._board) for r in range(3)]
        return  '\n----------\n'.join(rows)