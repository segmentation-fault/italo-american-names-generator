__author__ = 'antonio franco'

'''
Copyright (C) 2019  Antonio Franco (antonio_franco@live.it)
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''

from faker import Faker


class ItUsGen(object):
    def __init__(self) -> None:
        """
        Generates random italo-american names using faker. It only generates "simple" names, comprised of name and
        surname each one composed by a single word (no titles too).
        """
        super().__init__()
        self.fakeIt = Faker('it_IT')
        self.fakeUs = Faker('en_US')
        self.next_name = None  # To store the second element of the pair of names

    def __gen_next_tuple__(self) -> tuple:
        """
        Creates two italo-american names
        :return: tuple of strings (name1, name2)
        """
        list_it = []
        list_us = []

        # We discard composite names, like "Luca De Angelis" or "Sig.ra Marta Rossi"
        while len(list_it) != 2 or len(list_us) != 2:
            name_it = self.fakeIt.name()
            name_us = self.fakeUs.name()

            list_it = name_it.split()
            list_us = name_us.split()

            name1 = list_it[0] + ' ' + list_us[1]
            name2 = list_us[0] + ' ' + list_it[1]

        return name1, name2

    def gen_next(self) -> str:
        """
        Creates one italo-american name
        :return (str): next italo-american name
        """
        ret = self.next_name
        if self.next_name is None:
            (name1, name2) = self.__gen_next_tuple__()
            ret = name1
            self.next_name = name2
        else:
            self.next_name = None

        return ret

    def dump_txt(self, num_names: int, out_file: str) -> None:
        """
        Generates num_names italo-american names and dumps them in the file with path out_file, each on a different line
        :param num_names (int): number of italo-american names to write
        :param out_file (str):  path of the output file
        """
        f = open(out_file, "w+")
        for i in range(0, num_names):
            f.write(self.gen_next() + "\n")

        f.close()


if __name__ == "__main__":
    # Generates 1000 italo-american names and dumps them in "it_us_names.txt"
    G = ItUsGen()

    G.dump_txt(1000, "it_us_names.txt")
