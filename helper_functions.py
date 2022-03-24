import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager

import lp_text


def print_section_info(input_array):
    print(f"Section contains {len(input_array)} runes.")


def calculate_ioc(input_array):
    _, counts = np.unique(input_array, return_counts=True)
    ioc = 0

    for counted in counts:
        ioc += counted * (counted - 1)
    ioc = ioc / (len(input_array) * (len(input_array) - 1) / 29)

    print(ioc)


def count_doublets(input_array):
    number_of_doublets = np.sum(input_array[0:-1] == input_array[1::])
    print(f"Number of doublets: {number_of_doublets}")
    print(f"Doublets rate: {number_of_doublets / (len(input_array) - 1) * 100}%")


def plot_bigrams(input_array, axis_option=None, fullscreen=None):
    matplotlib.rcParams['font.family'] = "Segoe UI Historic"

    bigram_table = np.zeros((29, 29), dtype=np.int32)
    if isinstance(input_array, list):
        for element in input_array:
            for index in range(len(element) - 1):
                bigram_table[element[index + 1], element[index]] += 1
    else:
        for index in range(len(input_array) - 1):
            bigram_table[input_array[index + 1], input_array[index]] += 1

    fig, ax = plt.subplots()
    ax.matshow(bigram_table, cmap=plt.cm.rainbow)
    sx = ax.secondary_xaxis('bottom')
    sy = ax.secondary_yaxis('right')

    ax.set_xticks(np.arange(29))
    ax.set_yticks(np.arange(29))
    sx.set_xticks(np.arange(29))
    sy.set_yticks(np.arange(29))

    ax.set_xticklabels(latin_ticks())
    ax.set_yticklabels(latin_ticks())

    if axis_option == 'runes':
        sx.set_xticklabels(rune_ticks())
        sy.set_yticklabels(rune_ticks())

    plt.title('Pages 0 to 55, 12956 runes, bigram count', fontsize=25)
    ax.set_xlabel('First rune')
    ax.xaxis.set_label_position('top')
    plt.ylabel('Second rune')

    for i in range(29):
        for j in range(29):
            c = bigram_table[j, i]
            ax.text(i, j, str(c), va='center', ha='center')

    if fullscreen:
        plot_fullscreen()

    gcf = plt.gcf()
    plt.show()
    gcf.savefig('C:/Users/Heinricp/PycharmProjects/cipher_statistics/bigram_table.png', bbox_inches='tight')


def plot_letter_frequency(input_array, axis_option=None):
    matplotlib.rcParams['font.family'] = "Segoe UI Historic"

    _, counts = np.unique(input_array, return_counts=True)
    if len(counts) != 29:
        counts = np.zeros(29)
        for number in range(29):
            counts[number] = np.sum(input_array == number)
    fig, ax = plt.subplots()
    plt.plot(np.arange(29), counts)
    ax.set_xticks(np.arange(29))
    ax.set_xlim(left=0, right=28)

    if axis_option == 'runes':
        ax.set_xticklabels(rune_ticks())
    if axis_option == 'latin':
        ax.set_xticklabels(latin_ticks())

    plt.tight_layout()


def latin_ticks():
    return ['F', 'V', 'TH', 'O', 'R', 'C', 'G', 'W', 'H', 'N', 'I', 'J', 'EO', 'P', 'X', 'S', 'T', 'B', 'E', 'M', 'L', 'ING', 'OE',
            'D', 'A', 'AE', 'Y', 'IA', 'EA']


def rune_ticks():
    return ['ᚠ', 'ᚢ', 'ᚦ', 'ᚩ', 'ᚱ', 'v', 'ᚷ', 'ᚹ', 'ᚻ', 'ᚾ', 'ᛁ', 'ᛄ', 'ᛇ', 'ᛈ', 'ᛉ', 'ᛋ', 'ᛏ', 'ᛒ', 'ᛖ', 'ᛗ', 'ᛚ', 'ᛝ', 'ᛟ', 'ᛞ',
            'ᚪ', 'ᚫ', 'ᚣ', 'ᛡ', 'ᛠ ']


def plot_fullscreen():
    manager = plt.get_current_fig_manager()
    manager.window.showMaximized()


def convert_text_to_index(input_text):
    latin_fragments = ['F', 'U', 'TH', 'O', 'R', 'C', 'G', 'W', 'H', 'N', 'I', 'J', 'EO', 'P', 'X', 'S', 'T', 'B', 'E', 'M', 'L', 'ING',
                       'OE',
                       'D', 'A', 'AE', 'Y', 'IA', 'EA']

    e2p = {}
    for i in range(0, 29):
        e2p[latin_fragments[i]] = i
    e2p["IO"] = e2p["IA"]
    e2p["K"] = e2p["C"]
    e2p["NG"] = e2p["ING"]
    e2p["Z"] = e2p["S"]
    e2p["Q"] = e2p["C"]
    e2p["V"] = e2p["U"]

    input_text = input_text.upper().replace("QU", "KW")
    input_text = input_text.replace("Q", "K")

    text_as_index = []
    skip = 0
    for index, value in enumerate(input_text):
        if skip:
            skip -= 1
            continue
        if input_text[index:index + 3] in e2p:
            text_as_index.append(e2p[input_text[index:index + 3]])
            skip = 2
            continue
        elif input_text[index:index + 2] in e2p:
            text_as_index.append(e2p[input_text[index:index + 2]])
            skip = 1
        else:
            text_as_index.append(e2p[input_text[index]])
    return np.asarray(text_as_index)


def search_sequence_numpy(arr, seq):
    """ Find sequence in an array using NumPy only.

    Parameters
    ----------
    arr    : input 1D array
    seq    : input 1D array

    Output
    ------
    Output : 1D Array of indices in the input array that satisfy the
    matching of input sequence in the input array.
    In case of no match, an empty list is returned.
    """

    # Store sizes of input array and sequence
    Na, Nseq = arr.size, seq.size

    # Range of sequence
    r_seq = np.arange(Nseq)

    # Create a 2D array of sliding indices across the entire length of input array.
    # Match up with the input sequence & get the matching starting indices.
    M = (arr[np.arange(Na - Nseq + 1)[:, None] + r_seq] == seq).all(1)

    # Get the range of those indices as final output
    if M.any() > 0:
        return np.where(np.convolve(M, np.ones((Nseq), dtype=int)) > 0)[0]
    else:
        return []


def find_repeats(ct, len_repeats):
    for i in range(len(ct) - len_repeats):
        a = search_sequence_numpy(ct, ct[i:i + len_repeats])
        if len(a) > len_repeats:
            return 1
    return 0


def find_rune_repeats_on_page(input_text):
    x = lp_text.unsolved_pages_from_wiki()
    for page_number, page_content in enumerate(x):
        if input_text in page_content:
            print(page_number)
