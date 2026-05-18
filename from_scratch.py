def naked_single(cell_list)

    for cell in cell_list:
        if cell.num_possible_values() == 1:
            return cell
        
    return None