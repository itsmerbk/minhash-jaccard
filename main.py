import hashlib

def minhash_sig(tokens, num_hashes=32):
    sig = []
    for i in range(num_hashes):
        sig.append(min(int(hashlib.sha256(f"{i}:{t}".encode()).hexdigest()[:12], 16) for t in tokens))
    return sig

def jaccard_est(sig_a, sig_b):
    return sum(1 for a, b in zip(sig_a, sig_b) if a == b) / len(sig_a)

if __name__ == "__main__":
    s1 = minhash_sig({"distributed", "systems", "raft", "consensus"})
    s2 = minhash_sig({"distributed", "systems", "raft", "storage"})
    assert 0.4 <= jaccard_est(s1, s2) <= 0.85
    print("[PASS] 028_minhash_jaccard")
