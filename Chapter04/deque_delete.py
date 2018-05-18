def delete_nth(d, n):
    d.rotate(-n)
    d.popleft()
    d.rotate(n)
