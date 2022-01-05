
from typing import Dict, List
import matplotlib.pyplot as plt


def visualize(statistics: Dict[str, Dict[chr, List[float]]]):

    fixed_prob_color = 'tab:orange'
    csuros_color = 'tab:blue'

    fig, ((ax1,ax2),(ax3,ax4), (ax5,ax6), (ax7, ax8)) = plt.subplots(nrows=4, ncols=2)
    fig.subplots_adjust(hspace=0.4)
    ax8.set_visible(False)

    """
    # exact counts
    ax1.plot([key for key in statistics['exact_count'].keys()], [result[0] for result in statistics['exact_count'].values()], 'tab:green', label='exact')
    ax1.plot([key for key in statistics['min'].keys()], [results[0] for results in statistics['min'].values()], fixed_prob_color, linestyle='--', label='Fixed-Prob')
    ax1.plot([key for key in statistics['max'].keys()], [results[0] for results in statistics['max'].values()], fixed_prob_color, linestyle='--')
    ax1.plot([key for key in statistics['min'].keys()], [results[1] for results in statistics['min'].values()], csuros_color, linestyle='--', label='Csuros')
    ax1.plot([key for key in statistics['max'].keys()], [results[1] for results in statistics['max'].values()], csuros_color, linestyle='--')
    ax1.set_title('Counts')
    ax1.set_ylabel('value')
    ax1.set_xlabel('characters')
    ax1.legend()

    # accuracy
    ax2.plot([key for key in statistics['accuracy'].keys()], [results[0] for results in statistics['accuracy'].values()], fixed_prob_color, label='Fixed-Prob')
    ax2.plot([key for key in statistics['accuracy'].keys()], [results[1] for results in statistics['accuracy'].values()], csuros_color, label='Csuros')
    ax2.set_title('Accuracy')
    ax2.set_ylabel('percentage (%)')
    ax2.set_xlabel('characters')
    ax2.legend()

    # max_deviation
    ax3.plot([key for key in statistics['max_deviation'].keys()], [results[0] for results in statistics['max_deviation'].values()], fixed_prob_color, label='Fixed-Prob')
    ax3.plot([key for key in statistics['max_deviation'].keys()], [results[1] for results in statistics['max_deviation'].values()], csuros_color, label='Csuros')
    ax3.set_title('Maximum Deviation')
    ax3.set_ylabel('value')
    ax3.set_xlabel('characters')
    ax3.legend()

    # MAD
    ax4.plot([key for key in statistics['mad'].keys()], [results[0] for results in statistics['mad'].values()], fixed_prob_color, label='Fixed-Prob')
    ax4.plot([key for key in statistics['mad'].keys()], [results[1] for results in statistics['mad'].values()], csuros_color, label='Csuros')
    ax4.set_title('Mean Absolute Deviation')
    ax4.set_ylabel('value')
    ax4.set_xlabel('characters')
    ax4.legend()

    # MAE
    ax5.plot([key for key in statistics['mae'].keys()], [results[0] for results in statistics['mae'].values()], fixed_prob_color, label='Fixed-Prob')
    ax5.plot([key for key in statistics['mae'].keys()], [results[1] for results in statistics['mae'].values()], csuros_color, label='Csuros')
    ax5.set_title('Mean Absolute Error')
    ax5.set_ylabel('value')
    ax5.set_xlabel('characters')
    ax5.legend()
    """

    # MRE
    """
    ax6.plot([key for key in statistics['mre'].keys()], [results[0] for results in statistics['mre'].values()], fixed_prob_color, label='Fixed-Prob')
    ax6.plot([key for key in statistics['mre'].keys()], [results[1] for results in statistics['mre'].values()], csuros_color, label='Csuros')
    ax6.set_title('Mean Relative Error')
    ax6.set_ylabel('percentage (%)')
    ax6.set_xlabel('characters')
    ax6.legend()
    """
    
    # Bits
    ax6.plot([key for key in statistics['num_bits'].keys()], [results[0] for results in statistics['num_bits'].values()], fixed_prob_color, label='Fixed-Prob')
    ax6.plot([key for key in statistics['num_bits'].keys()], [results[1] for results in statistics['num_bits'].values()], csuros_color, label='Csuros')
    ax6.set_title('Bits')
    ax6.set_ylabel('value')
    ax6.set_xlabel('characters')
    ax6.legend()

    plt.show()
