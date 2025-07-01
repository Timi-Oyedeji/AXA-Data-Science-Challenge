# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 17:36:43 2020
@name:
    plot_essences.py
@env:
    Python 3.7.0
@auth: 
    steph
@desc:
    description here
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.legend as mlegend
from matplotlib.patches import Rectangle
from mpl_toolkits.axes_grid1.inset_locator import InsetPosition, mark_inset, inset_axes
from matplotlib import cm
from matplotlib.colors import ListedColormap, LinearSegmentedColormap

linewidth = 1

def sans_init():
    plt.rcParams['font.family'] = "sans-serif"
    plt.rcParams['font.sans-serif'] = "arial"
    # plt.rcParams['mathtext.fontset'] = "stixsans" # can be cm='computer modern', stix = 'stix' (times), stixsans= 'stix sans-serif'
    # stixsans has bold greek and can be done as "\mathbf{\sigma}"
    plt.rcParams['mathtext.fontset'] = 'custom'
    plt.rcParams['mathtext.it'] = 'Arial:italic'
    plt.rcParams['mathtext.bf'] = 'Arial:bold'
    plt.rcParams['mathtext.sf'] = 'Arial:italic:bold'
    plt.rcParams['text.usetex'] = False

def latex_init():
    plt.rcParams['text.usetex'] = True


def simple_plot_init(Axis_Label=['',''], font_size=10, bold_label=True, xlabelpad=None, ylabelpad=None, **kwargs):
    #Then, "ALWAYS use Arial fonts"
    scale = font_size/10
    
    fig = plt.figure(**kwargs)
    ax = fig.add_subplot(111)
    
    bold = 'bold' if bold_label else None

    ax.set_xlabel(Axis_Label[0],size = font_size, fontweight=bold, labelpad=xlabelpad)
    ax.set_ylabel(Axis_Label[1],size = font_size, fontweight=bold, labelpad=ylabelpad)

    ax.minorticks_on()
    ax.tick_params(axis='both',which='major',width=linewidth,length=3*scale,labelsize=font_size*0.8)
    ax.tick_params(axis='both',which='minor',width=linewidth,length=1.8*scale,labelsize=font_size*0.8)

    axes=plt.gca();  #get axis' handle
    axes.spines['bottom'].set_linewidth(linewidth);  # bottom linewidth
    axes.spines['left'].set_linewidth(linewidth);    # left linewidth
    axes.spines['right'].set_linewidth(linewidth);   # right linewidth
    axes.spines['top'].set_linewidth(linewidth);     # top linewidth
    
    ax.ticklabel_format(useMathText=True)
    offset_text = ax.yaxis.get_offset_text()
    
    offset_text.set_size(font_size*0.8)
    
    return fig, ax


def simple_twinx_plot_init(Axis_Label=['','',''], font_size=10, xlabelpad=None, y1labelpad=None, y2labelpad=None, **kwargs):
    #Then, "ALWAYS use Arial fonts" 
    scale = font_size/10
    
    fig = plt.figure(**kwargs)
    ax = fig.add_subplot(111)
    ax2 = ax.twinx()
    
    ax.set_xlabel(Axis_Label[0], size = font_size, fontweight='bold', labelpad=xlabelpad)
    ax.set_ylabel(Axis_Label[1], size = font_size, fontweight='bold', labelpad=y1labelpad)
    ax2.set_ylabel(Axis_Label[2], size = font_size, fontweight='bold', labelpad=y2labelpad)

    ax.minorticks_on()
    ax.tick_params(axis='both',which='major',width=linewidth,length=3*scale,labelsize=font_size*0.8)
    ax.tick_params(axis='both',which='minor',width=linewidth,length=1.8*scale,labelsize=font_size*0.8)
    
    ax2.minorticks_on()
    ax2.tick_params(axis='both',which='major',width=linewidth,length=3*scale,labelsize=font_size*0.8)
    ax2.tick_params(axis='both',which='minor',width=linewidth,length=1.8*scale,labelsize=font_size*0.8)

    axes=plt.gca();  #get axis' handle
    axes.spines['bottom'].set_linewidth(linewidth);  # bottom linewidth
    axes.spines['left'].set_linewidth(linewidth);    # left linewidth
    axes.spines['right'].set_linewidth(linewidth);   # right linewidth
    axes.spines['top'].set_linewidth(linewidth);     # top linewidth
    
    ax.ticklabel_format(useMathText=True)
    offset_text_ax1 = ax.yaxis.get_offset_text()
    offset_text_ax1.set_size(font_size*0.8)
    
    ax2.ticklabel_format(useMathText=True)
    offset_text_ax2 = ax2.yaxis.get_offset_text()
    offset_text_ax2.set_size(font_size*0.8)
    
    return fig, ax, ax2


#  all_legends(fig, **kwargs)
#--------------------------------------------------------------
#  Put all legends of all axes together
# 
 
def all_legends(fig, **kwargs):
        lines, labels = (list(),list())
        for ax in fig.axes:
            axLine, axLabel = ax.get_legend_handles_labels()
            lines.extend(axLine)
            labels.extend(axLabel)  
        fig.legend(lines, labels, **kwargs)


#  tablelegend(ax, col_labels=None, row_labels=None, title_label="", *args, **kwargs)
#--------------------------------------------------------------
#  Place a table legend on the axes.

#  Creates a legend where the labels are not directly placed with the artists,
#  but are used as row and column headers, looking like this:

#  title_label   | col_labels[1] | col_labels[2] | col_labels[3]
#  -------------------------------------------------------------
#  row_labels[1] |
#  row_labels[2] |              
#  row_labels[3] |


#  Parameters
#  ----------

#  ax : `matplotlib.axes.Axes`
#      The artist that contains the legend table, i.e. current axes instant.

#  col_labels : list of str, optional
#      A list of labels to be used as column headers in the legend table.
#      `len(col_labels)` needs to match `ncol`.

#  row_labels : list of str, optional
#      A list of labels to be used as row headers in the legend table.
#      `len(row_labels)` needs to match `len(handles) // ncol`.

#  title_label : str, optional
#     Label for the top left corner in the legend table.

#  ncol : int
#      Number of columns.


#  Other Parameters
#  ----------------

#  Refer to `matplotlib.legend.Legend` for other parameters.

def tablelegend(ax, col_labels=None, row_labels=None, title_label="", *args, **kwargs):

    #################### same as `matplotlib.axes.Axes.legend` #####################
    handles, labels, extra_args, kwargs = mlegend._parse_legend_args([ax], *args, **kwargs)
    if len(extra_args):
        raise TypeError('legend only accepts two non-keyword arguments')
    
    if col_labels is None and row_labels is None:
        ax.legend_ = mlegend.Legend(ax, handles, labels, **kwargs)
        ax.legend_._remove_method = ax._remove_legend
        return ax.legend_
    #################### modifications for table legend ############################
    else:
        ncol = kwargs.pop('ncol')
        handletextpad = kwargs.pop('handletextpad', 0 if col_labels is None else -2)
        title_label = [title_label]
    
        # blank rectangle handle
        extra = [Rectangle((0, 0), 1, 1, fc="w", fill=False, edgecolor='none', linewidth=0)]
    
        # empty label
        empty = [""]
    
        # number of rows infered from number of handles and desired number of columns
        nrow = len(handles) // ncol
    
        # organise the list of handles and labels for table construction
        if col_labels is None:
            assert nrow == len(row_labels),"nrow = len(handles) // ncol = %s, but should be equal to len(row_labels) = %s." % (nrow, len(row_labels))
            leg_handles = extra * nrow
            leg_labels  = row_labels
        elif row_labels is None:
            assert ncol == len(col_labels),"ncol = %s, but should be equal to len(col_labels) = %s." % (ncol, len(col_labels))
            leg_handles = []
            leg_labels  = []
        else:
            assert nrow == len(row_labels),"nrow = len(handles) // ncol = %s, but should be equal to len(row_labels) = %s." % (nrow, len(row_labels))
            assert ncol == len(col_labels),"ncol = %s, but should be equal to len(col_labels) = %s." % (ncol, len(col_labels))
            leg_handles = extra + extra * nrow
            leg_labels  = title_label + row_labels
        
        leg_handles_print = []
        leg_labels_print = []
        for col in range(ncol):
            if col_labels is not None:
                leg_handles_print  += extra
                leg_labels_print   += [col_labels[col]]
            leg_handles_print  += handles[col*nrow:(col+1)*nrow]
            leg_labels_print   += empty * nrow
        leg_handles_print += leg_handles
        leg_labels_print += leg_labels
        # Create legend
        ax.legend_ = mlegend.Legend(ax, leg_handles_print, leg_labels_print, ncol = ncol+int(row_labels is not None), 
                                    handletextpad = handletextpad, **kwargs)
        ax.legend_._remove_method = ax._remove_legend
        return ax.legend_
    


def simple_inset_zoomin(ax, ins_xlength, ins_ylength, ins_x, ins_y, bbox_offsetx=0, bbox_offsety=0, font_size=10, **kwargs):
    scale = font_size/10
    # axins = inset_axes(ax, [1-ins_xlength,1-ins_ylength,ins_xlength,ins_ylength], height='40%', **kwargs)
    axins = inset_axes(ax, width="%i%%"%(ins_xlength*100), height="%i%%"%(ins_ylength*100), **kwargs)
    xmin = ins_x[0]
    xmax = (1+bbox_offsetx) * ins_x[-1]
    ymin = ins_y[0]
    ymax = (1+bbox_offsety) * ins_y[-1]
    axins.set_xlim(xmin, xmax)
    axins.set_ylim(ymin, ymax)

    axins.minorticks_on()
    axins.tick_params(axis='both',which='major', width=linewidth, 
                      length=3*scale, labelsize=font_size)
    axins.tick_params(axis='both',which='minor', width=linewidth, 
                      length=1.8*scale, labelsize=font_size)
    
    ## set sci notation
    axins.ticklabel_format(useMathText=True)
    offset_text = axins.yaxis.get_offset_text()
    offset_text.set_size(font_size)
    return axins

'''
Parameters
----------

ax : `matplotlib.figure.Figure`

ins_xlength :  `float`
               x-axis relatvie length (in percentage) of the inset cf. fig 

ins_ylength :  `float`
               y-axis relatvie length (in percentage) of the inset cf. fig 

ins_x :  `float`
               x-axis relatvie coord (in percentage) of the inset's bottom-left cf. fig 

ins_y :  `float`
               y-axis relatvie coord (in percentage) of the inset's top-right cf. fig 

Axis_Label :  `list` of `str`, optional

lpx: `float`
     labelpad of the inset's x-axis 

lpy: `float`
     labelpad of the inset's y-axis 

'''
def simple_inset(fig, ins_xlength, ins_ylength, ins_x, ins_y, Axis_Label=[None,None], 
        lpx = 0, lpy = 0, bold_label = True, font_size=10, **kwargs):
    scale = font_size/10
    ax2 = fig.add_axes([ins_x, ins_y, ins_xlength, ins_ylength])

    ax2.minorticks_on()
    ax2.tick_params(axis='both',which='major', width=linewidth, 
                      length=3*scale, labelsize=font_size)
    ax2.tick_params(axis='both',which='minor', width=linewidth, 
                      length=1.8*scale, labelsize=font_size)

    bold = 'bold' if bold_label else None
    ax2.set_xlabel(Axis_Label[0],size = font_size, labelpad=lpx, fontweight=bold)
    ax2.set_ylabel(Axis_Label[1],size = font_size, labelpad=lpy, fontweight=bold)
    return ax2


def simple_bar_init(Axis_Label=['',''], font_size=8, **kwargs):
    #Then, "ALWAYS use Arial fonts"
    scale = font_size/10
    
    fig = plt.figure(**kwargs)
    ax = fig.add_subplot(111)
    
    plt.xlabel(Axis_Label[0],size = font_size, fontweight='bold')
    plt.ylabel(Axis_Label[1],size = font_size, fontweight='bold')
    
    ax.tick_params(axis='both',which='major',width=linewidth,length=3*scale,labelsize=font_size*0.8)

    axes=plt.gca();  #get axis' handle
    axes.spines['bottom'].set_linewidth(linewidth);  # bottom linewidth
    axes.spines['left'].set_linewidth(linewidth);    # left linewidth
    axes.spines['right'].set_linewidth(linewidth);   # right linewidth
    axes.spines['top'].set_linewidth(linewidth);     # top linewidth

    ax.minorticks_on()
    ax.tick_params(axis='both',which='major',width=linewidth,length=3*scale,labelsize=font_size*0.8)
    ax.tick_params(axis='both',which='minor',width=linewidth,length=1.8*scale,labelsize=font_size*0.8)
    
    ax.ticklabel_format(useMathText=True)
    offset_text = ax.yaxis.get_offset_text()
    
    offset_text.set_size(font_size*0.8)

    ax.tick_params(axis='x', which='minor', bottom=False)
    
    return fig, ax

#  colormaps
#--------------------------------------------------------------

memer_colormap={
    'memer_simple': ['red', 'blue', 'orange', '#2f7edd', '#ea5514'],
    'sat_rainbow': ['#a40000', '#ea5514', 'orange', '#8fc31f', '#00913a', '#2f7edd', '#0303b8'],
    'desat_rainbow': ['#e84b42', '#e67e25',  '#f2c313', '#2fcd70', '#19bc9f', '#3198db', '#9c59b8'],
    'desat_rainbow_dark':['#c0382a', '#d35701', '#f49d12', '#28ac61', '#16a089', '#2c7eb8', '#8f42a8'],
    'sequential_red':['#eb6877', 'red', '#a40000']
}

def get_memer_cmap(name, num=100):
    return LinearSegmentedColormap.from_list(name, memer_colormap[name], N=num)

def simple_colorlist(name='memer_simple'):
    return memer_colormap[name]

def colorlist_mapping(cmap, num):
    return cmap(np.linspace(0, 1, num))


#  simple_canvas
#--------------------------------------------------------------
def linewidth_from_data_units(linewidth, axis, reference='y'):
    """
    Convert a linewidth in data units to linewidth in points.

    Parameters
    ----------
    linewidth: float
        Linewidth in data units of the respective reference-axis
    axis: matplotlib axis
        The axis which is used to extract the relevant transformation
        data (data limits and size must not change afterwards)
    reference: string
        The axis that is taken as a reference for the data width.
        Possible values: 'x' and 'y'. Defaults to 'y'.

    Returns
    -------
    linewidth: float
        Linewidth in points
    """
    fig = axis.get_figure()
    if reference == 'x':
        length = fig.bbox_inches.width * axis.get_position().width
        value_range_list = np.diff(axis.get_xlim())
    elif reference == 'y':
        length = fig.bbox_inches.height * axis.get_position().height
        value_range_list = np.diff(axis.get_ylim())
    value_range = value_range_list.item()
    ### Convert length to points
    # why 72 is the correct number: The linewidth is given in points.
    # The points unit is commonly 72 points/inch, also in matplotlib. While the dots per inch may change, points per inch stay constant.
    length *= 72
    # Scale linewidth to value range
    return linewidth * (length / value_range)

def simple_canvas(size=[None,None], scale_factor=2.5, dpi=150, background='black', from_center=False, **kwargs):
    x, y = (size[0], size[1])
    size_x = scale_factor*x/y
    size_y = scale_factor
    # pt to px
    DPI = dpi
    fig = plt.figure(figsize=[size_x,size_y],dpi=DPI,facecolor=background, **kwargs)
    ax = fig.add_subplot(111)
    if from_center:
        plt.xlim(-x/2, x/2)
        plt.ylim(-y/2, y/2)
    else:
        plt.xlim(0, x)
        plt.ylim(0, y)
    plt.axis('off')
    return fig, ax

