import os
import zlib


def compress_random_string(length):

    # Generate a long random string
    random_string = os.urandom(length)

    # Compress
    compressed_string = zlib.compress(random_string)

    # compression ratio
    compression_ratio = len(compressed_string) / len(random_string)

    return {
        "random_string_length": len(random_string),
        "compressed_string_length": len(compressed_string),
        "compression_ratio": compression_ratio,
    }


if __name__ == "__main__":
    length = 1024
    result = compress_random_string(length)
    print(f"Random string length: {result['random_string_length']} bytes")
    print(f"Compressed string length: {result['compressed_string_length']} bytes")
    print(f"Compression ratio: {result['compression_ratio']}")
