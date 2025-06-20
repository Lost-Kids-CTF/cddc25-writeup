# Encoder

## Challenge (??? points, ??? solves)

We've found Cypher's string encoder and encoded strings.
Can you recover the original string?

Encoded string:
MEi4xJpC4pI+FiJuAn4i2o7hpfHVCavRpfkzp18rX99jwWdodAA0wHQAYtKO9noGdBJ2sg==

Flag format: CDDC2025{   }

## Summary

This challenge provides an Elixir `.beam` file (`Elixir.Encoder.beam`) and a Base64-encoded string. The goal is to reverse the encoding logic embedded in the compiled Elixir code and recover the original plaintext (i.e., the flag).

## Analysis

The `.beam` file is a compiled Elixir module. To reverse-engineer it, we can use [`beam_to_ex`](https://github.com/olafura/beam_to_ex) to decompile the BEAM bytecode back into readable Elixir code.

```elixir
defmodule Encoder do
  def main() do
    _args = System.argv()

    case _args do
      [_text | _] ->
        _encoded = :base64.encode_to_string(encode(_text))

        IO.puts(
          "Encoded: " <>
            case _encoded do
              [& &1, &String.Chars.to_string(&1)]
            end
        )

      [] ->
        print_usage()
    end
  end

  def print_usage() do
    IO.puts("Usage: encryptor <plain>")
  end

  def encode(_input) do
    _base_key = 66

    list_to_binary(
      Enum.map(
        Enum.with_index(String.to_charlist(_input)),
        fn {_char, _index} ->
          _xored = bxor(_char, _base_key)
          _position_key = rem(_index * 7 + 13, 256)
          _position_xored = bxor(_xored, _position_key)
          _final = reverse_bits(_position_xored)
          _final
        end
      )
    )
  end

  def reverse_bits(_byte) do
    Enum.reduce(%{__struct__: Range, first: 0, last: 7, step: 1}, 0, fn _i, _acc ->
      _bit = bsr(band(_byte, bsl(1, _i)), _i)
      bor(_acc, bsl(_bit, 7 - _i))
    end)
  end
end
```

The recovered Elixir source shows an `encode/1` function which:

1. Converts the input string to a list of characters.
2. For each character:
   * XORs it with a fixed key (66).
   * Applies a position-dependent XOR: `(index * 7 + 13) % 256`.
   * Reverses the bits of the result.
3. Returns the resulting bytes as a Base64-encoded string.

To decrypt, we simply reverse each step in the reverse order.

## Approach

### Step 1: Understand the encoding

Using the decompiled Elixir code, we identified the following transformations per byte:

* `rev_bits(bxor(bxor(char, 66), pos_key))`

### Step 2: Implement decode

We wrote a Python script to reverse these transformations:

* Reverse the bits (using a precomputed lookup table).
* XOR with position-dependent key.
* XOR with the fixed base key `66`.

See `solve.py`.

## Flag

`CDDC2025{fUncTioNAl_pr0gRaMmiNg_i5_VeRy_In73reSt1nG}`
