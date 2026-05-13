

optab = {
    "START": ("AD", "01"),
    "END": ("AD", "02"),
    "MOVER": ("IS", "04"),
    "ADD": ("IS", "05"),
    "SUB": ("IS", "06"),
    "MULT": ("IS", "07"),
    "DC": ("DL", "01"),
    "DS": ("DL", "02")
}

symtab = {}
littab = []
intermediate = []
LC = 0

# ----- Read from input.txt -----
with open("input.txt", "r") as f:
    lines = [line.strip() for line in f if line.strip()]

# ----- Pass I -----
for line in lines:
    parts = line.split()
    label, opcode, operand = "", "", ""

    if len(parts) == 3:
        label, opcode, operand = parts
    elif len(parts) == 2:
        opcode, operand = parts
    elif len(parts) == 1:
        opcode = parts[0]

    if opcode.upper() == "START":
        LC = int(operand)
        intermediate.append(f"{LC}\t{line}")
        continue

    if opcode.upper() == "END":
        intermediate.append(f"{LC}\t{line}")
        break

    if label:
        symtab[label] = LC

    if operand.startswith("="):
        littab.append(operand)

    intermediate.append(f"{LC}\t{line}")
    LC += 1

# ----- Assign addresses to literals -----
for i, lit in enumerate(littab):
    littab[i] = (lit, LC + i)

# ----- Write Outputs -----
with open("intermediate.txt", "w") as f:
    f.write("INTERMEDIATE CODE:\n")
    for line in intermediate:
        f.write(line + "\n")

with open("symtab.txt", "w") as f:
    f.write("SYMBOL TABLE:\n")
    for s, addr in symtab.items():
        f.write(f"{s}\t{addr}\n")

with open("littab.txt", "w") as f:
    f.write("LITERAL TABLE:\n")
    for lit, addr in littab:
        f.write(f"{lit}\t{addr}\n")

print("✅ PASS-I Completed Successfully!")
print("Files generated: intermediate.txt, symtab.txt, littab.txt")

