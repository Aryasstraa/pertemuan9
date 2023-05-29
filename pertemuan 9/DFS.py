import os
os.system('cls')
# Menentukan tree
tree = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': [],
    'F': [],
    'G': []
}

# Tentukan fungsi DFS 
def DFS(tree, node):
    # Inisialisasi antrian dan set yang dikunjungi
    stack = []
    visited = set()

    # Tambahkan simpul awal ke tumpukan dan set yang dikunjungi
    stack.append(node)
    visited.add(node)

    # Ulangi tumpukan sampai kosong
    while stack:
        
        # Hapus elemen terakhir dari tumpukan
        node = stack.pop()
        print(node, end=' ')
        # Tambahkan node anak dari node saat ini ke tumpukan dan set yang dikunjungi
        
        for child in tree[node]:
            if child not in visited:
                stack.append(child)
                visited.add(child)

# Panggil fungsi DFS 
DFS(tree, 'A')


