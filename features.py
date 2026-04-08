def extract_features(url):
    features = []
    reasons = []
    
    # Length
    features.append(len(url))
    if len(url) > 50:
        reasons.append("URL is too long")
    
    # HTTPS
    features.append(1 if "https" in url else 0)
    if "https" not in url:
        reasons.append("Not secure (no HTTPS)")
    
    # Dots
    features.append(url.count('.'))
    if url.count('.') > 3:
        reasons.append("Too many dots in URL")
    
    # @ symbol
    features.append(1 if '@' in url else 0)
    if '@' in url:
        reasons.append("Contains @ symbol")
    
    # Suspicious words
    suspicious = ['login', 'verify', 'bank', 'secure']
    has_suspicious = any(word in url for word in suspicious)
    features.append(1 if has_suspicious else 0)
    
    if has_suspicious:
        reasons.append("Contains suspicious words")
    
    return features, reasons