class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        
        bulls = 0  # Number of bulls
        cows = 0   # Number of cows
        
        freq_secret = {}  # Frequency of digits in secret
        freq_guess = {}   # Frequency of digits in guess
        
        for s, g in zip(secret, guess):
            if s == g:
                bulls += 1
            else:
                freq_secret[s] = freq_secret.get(s, 0) + 1
                freq_guess[g] = freq_guess.get(g, 0) + 1
        
        for key in freq_secret:
            if key in freq_guess:
                cows += min(freq_secret[key], freq_guess[key])
        
        return f"{bulls}A{cows}B"