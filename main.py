import helper_functions as hpf
import lp_text as lp
import testing_texts as tt
import book_texts as bt
import encryption as enc
import numpy as np

if __name__ == '__main__':
    ct = lp.get_unsolved_pages(return_type='list')
    # hpf.print_section_info(ct)
    # hpf.calculate_ioc(ct)
    # hpf.count_doublets(ct)
    # hpf.find_repeats(ct,5)
    # hpf.find_rune_repeats_on_page("ᛗᛝᚣᚪᚫ")
    # hpf.plot_bigrams(ct, axis_option='runes',fullscreen=True)
    # hpf.plot_letter_frequency(ct, 'latin')
    # result = hpf.search_sequence_numpy(ct, np.array([1,0]))
    # print(f"Length: {len(result)/2}")
    # print(result)
    flag_counter = 0
    len_experiment = 1000
    for i in range(len_experiment):
        print(i)
        flag = hpf.find_repeats(np.random.randint(low=0, high=28, size=13000, dtype=np.int8), 6)
        flag_counter += flag
    print(f"Found {flag_counter} in {len_experiment} tries. This equals {flag_counter / len_experiment * 100}%")
