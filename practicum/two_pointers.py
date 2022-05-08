def get_next_dif_letter_idx(input_str, cur_letter_idx):
    next_letter_idx = cur_letter_idx
    while next_letter_idx < len(input_str) \
    and input_str[next_letter_idx] == input_str[cur_letter_idx]:
        next_letter_idx += 1
    return next_letter_idx

def max_consecutive_elements(input_str):
    result, cur_letter_idx = 0, 0
    while cur_letter_idx < len(input_str):
        next_letter_idx = get_next_dif_letter_idx(input_str, cur_letter_idx)
        result = max(result, next_letter_idx - cur_letter_idx)
        cur_letter_idx += 1
    return result
