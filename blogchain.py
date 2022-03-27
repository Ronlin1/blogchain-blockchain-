import hashlib

class BlogBlockToken:
    
    def __init__(self, previous_block_hash, transaction_list):

        self.previous_block_hash = previous_block_hash
        self.transaction_list = transaction_list

        self.block_data = f"{' <-> '.join(transaction_list)} <-> {previous_block_hash}"
        self.block_hash = hashlib.sha256(self.block_data.encode()).hexdigest()

class Blogchain:
    def __init__(self):
        self.chain = []
        self.generate_genesis_block()

    def generate_genesis_block(self):
        self.chain.append(BlogBlockToken("0", ['Genesis Block']))
    
    def create_block_from_transaction(self, transaction_list):
        previous_block_hash = self.last_block.block_hash
        self.chain.append(BlogBlockToken(previous_block_hash, transaction_list))

    def display_chain(self):
        for i in range(len(self.chain)):
            print(f"Data {i + 1}: {self.chain[i].block_data}")
            print(f"Hash {i + 1}: {self.chain[i].block_hash}")
            print("----------------------------------"
                  "\----------------------------------")

    @property
    def last_block(self):
        return self.chain[-1]
    
t1 = "George sends 3.1 BBT to Joe"
t2 = "Joe sends 2.5 BBT to Alice"
t3 = "Alice sends 1.2 BBT to Bob"
t4 = "Bob sends 0.5 BBT to Charlie"
t5 = "Charlie sends BBT GC to David"
t6 = "David sends 0.1 BBT to Eric"

my_blogchain = Blogchain()

my_blogchain.create_block_from_transaction([t1, t2])
my_blogchain.create_block_from_transaction([t3, t4])
my_blogchain.create_block_from_transaction([t5, t6])

my_blogchain.display_chain()

