class CompressedGene:
    def __init__(self, gene):
        self._compress(gene)

    def __str__(self):
        return self.decompress()

    def _compress(self, gene):
        self.bit_string = 1
        for nucleotide in gene.upper():
            self.bit_string <<= 2
            if nucleotide == "A":
                self.bit_string |= 0b00
            elif nucleotide == "C":
                self.bit_string |= 0b01
            elif nucleotide == "G":
                self.bit_string |= 0b10
            elif nucleotide == "T":
                self.bit_string |= 0b11
            else:
                raise ValueError(f"Invalide Nucleotide {nucleotide}")
    
    def decompress(self):
        gene = ""
        for i in range(0, self.bit_string.bit_length() - 1, 2):
            bits = self.bit_string >> i & 0b11
            if bits == 0b00:
                gene += "A"
            elif bits == 0b01:
                gene += "C"
            elif bits == 0b10:
                gene += "G"
            elif bits == 0b11:
                gene += "T"
            else:
                raise ValueError(f"Invalid bits: {bits}")
        return gene[::-1]

    
if __name__ == "__main__":
    from sys import getsizeof
    original = "ACGTCGTAGCTCGCGATATAGC" * 100
    print(original)
    print(f"Original is {getsizeof(original)}")
    comp = CompressedGene(original)

    print(comp)
    print(f"Compressed is {getsizeof(comp.bit_string)}")

    print(f"Original and compressed are the same: {original == comp.decompress()}")
