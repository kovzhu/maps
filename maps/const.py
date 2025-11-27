import datetime
import os
import requests
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from dotenv import load_dotenv
load_dotenv()
# from .utils.tools import get_excel_path

# define the paths used -----------------------------------------------------------------------------
class paths:
    """
    A class that defines and manages file system paths used in the CCUS project.

    This class handles path configuration for:
    - Current working directory
    - Database folder location
    - Output folder location
    - Map output location

    Methods:
        get_excel_path(): Locates the Excel file path for CCUS data

    Attributes:
        CURRENT_FOLDER (str): Path to current working directory
        DATABASE_FOLDER (str): Path to database folder containing Excel files
        OUTPUT_FOLDER (str): Path to output folder for generated files
        MAP_OUTPUT (str): Path to map output folder
    """
    research_topic = "Foreign companies in China_2025"

    def __init__(self) -> None:
        self.CURRENT_FOLDER = os.getcwd()
        # self.INSIGHTS_FOLDER = os.path.join(os.path.dirname(self.CURRENT_FOLDER),"10_Insight Memos")
        # self.RESEARCH_TOPIC_FOLDER = os.path.join(self.INSIGHTS_FOLDER,self.research_topic)
        # self.OUTPUT_FOLDER = os.path.join(self.CURRENT_FOLDER,'output')
        # self.MAP_OUTPUT =os.path.join(self.OUTPUT_FOLDER,'maps')




# FILE_PATH = os.getcwd()


# time stamps use in file names -----------------------------------------------------------------------
class timestamps:

    def __init__(self) -> None:
        self.timestamp_for_file_name = datetime.datetime.strftime(datetime.datetime.now(), "%Y%m%d-%H%M")
        self.timestampnn = datetime.datetime.strftime(datetime.datetime.now(), "%Y%m%d-%H%M%S")
        self.date_hour = datetime.datetime.strftime(datetime.datetime.now(),'%b%d-%H:%M')
        self.dateStamp = datetime.datetime.strftime(datetime.datetime.now(), "%Y-%m-%d")
        self.timestamp_for_archive = datetime.datetime.strftime(datetime.datetime.now(), "%d%b%Y")


# API keys -------------------------------------------------------------------------------------------
# class tokens:

#     def __init__(self) -> None:

#         # S&P Tokens
#         # self.CONNECT_KEY = os.getenv("CONNECT_KEY")
#         self.ICONA_KEY = os.getenv("ICONA_KEY")
#         self.CONNECT_AUTH = requests.auth.HTTPBasicAuth(
#             os.getenv("CONNECT_KEY"), os.getenv("CONNECT_PW")
#         )
#         self.SNOWFLAKE_ID = os.getenv("SNOWFLAKE_ID")
#         self.SNOWFLAKE_KEY = os.getenv("SNOWFLAKE_KEY")
#         self.SPARK_APP_ID = os.getenv("SPARK_APP_ID")
#         self.SPARK_API_KEY = os.getenv("SPARK_API_KEY")
#         self.GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
#         self.POWERTRAIN_TOKEN = os.getenv("POWERTRAIN_TOKEN")
#         self.CI_API_KEY = os.getenv("CI_API_KEY")

#         # External tokens
#         self.GEMINI_API_KEY = os.getevn("GEMINI_API_KEY")
#         self.DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")
#         self.QWEN_API_KEY = os.getenv("QWEN_API_KEY")
#         self.QWEN_API_KEY_CODING = os.getenv("QWEN_API_KEY_CODING")

# settings ===========================================================================================

# config the colors used in matplotlib
# SPG standard color pallet ----------------------------------------------------------------------------
class lists:

    def __init__(self) -> None:
        self.SPG_COLORS = ['#006D89','#F1A649','#782080','#54BAA0','#B92051','#AAB5DF','#1D3BAA','#B280B6','#C94100','#6DACBC','#501555','#CD6083','#125E1F','#9DCEA6','#9D5700','#E8AE92','#00495B','#EC8200','#6B0F01','#566CBF']
        self.YEAR_RANGE = list(range(1972,2040)) # used for generating annual addition chart


class SpglobalStyle:
    '''
    Axis: No tick marks; axis lines 0.75 pt, gray darker 35%. 
    Gridlines: None. 
    The font for axis: Arial, 10 pt. 
    For title: Arial (body), 12 pt.

    1 chart for a slide size: 
    fig, ax = plt.subplots(figsize=(4.75, 12.1))

    2 charts for a slide size
    fig, ax = plt.subplots(figsize=(4.75, 5.5))

    # sample use : Add labels and title
    ax.set_title('Stacked Bar Chart Example', pad=20)
    ax.set_ylabel('Values')
    ax.set_xlabel('Categories')

    # Add legend
    ax.legend()

    # Add footnote
    styling.add_footnote(fig)
    styling.apply_legend_style(ax,ncol=2)
    '''
    def __init__(self, 
                #  legend_loc: str ='best', 
                #  legend_bbox_to_anchor=None, 
                 font_family: str ='Arial', 
                 font_size: int =10, 
                 title_font_size: int =12)-> None:
        
        # self.legend_loc = legend_loc
        # self.legend_bbox_to_anchor = legend_bbox_to_anchor
        self.font_family = font_family
        self.font_size = font_size
        self.title_font_size = title_font_size
        self.set_defaults()
        # self.add_footnote()

    def set_defaults(self):

        # set axis style
        plt.rcParams['axes.prop_cycle'] = plt.cycler(color=LISTS.SPG_COLORS)
        plt.rcParams['axes.spines.top'] = False
        plt.rcParams['axes.spines.right'] = False
        plt.rcParams['axes.spines.bottom'] = True
        plt.rcParams['axes.spines.left'] = True
        plt.rcParams['axes.linewidth'] = 0.75
        # plt.rcParams['axes.edgecolor'] = 'gray'
        plt.rcParams['axes.edgecolor'] = '#595959'  # Gray darker 35%
        plt.rcParams['xtick.major.size'] = 0
        plt.rcParams['ytick.major.size'] = 0
        plt.rcParams['grid.linewidth'] = 0
        plt.rcParams['axes.labelcolor'] = 'black'
        plt.rcParams['xtick.color'] = 'black'
        plt.rcParams['ytick.color'] = 'black'
        plt.rcParams['axes.labelpad'] = 10 # Default padding (adjust as needed)

        # Legend Styling
        plt.rcParams['legend.frameon'] = False
        plt.rcParams['legend.title_fontsize'] = 0
        # plt.rcParams['legend.loc'] = self.legend_loc
        # if self.legend_bbox_to_anchor is not None:
        #     plt.rcParams['legend.bbox_to_anchor'] = self.legend_bbox_to_anchor

        # Font Settings (using parameters)
        try:
            plt.rcParams['font.family'] = self.font_family
        except fm.findfont(self.font_family):  # Check if font is found
            try:
                arial = fm.FontProperties(fname="C:/Windows/Fonts/arial.ttf")  # Windows
                plt.rcParams['font.family'] = arial.get_name()
            except FileNotFoundError:
                try:
                    dejavu = fm.FontProperties(fname="/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf")  # Linux
                    plt.rcParams['font.family'] = dejavu.get_name()
                except FileNotFoundError:
                    plt.rcParams['font.family'] = 'sans-serif'
                    print(f"Font '{self.font_family}' not found. Using sans-serif.")
            except ValueError:
                plt.rcParams['font.family'] = 'sans-serif'
                print(f"Font '{self.font_family}' not found. Using sans-serif.")

        plt.rcParams['font.size'] = self.font_size

        # Title Styling
        plt.rcParams['axes.titlesize'] = self.title_font_size
        plt.rcParams['axes.titleweight'] = 'bold'
        plt.rcParams['axes.titlelocation'] = 'left'

    def add_footnote(self, fig, left_text="Source: S&P Global Commodity Insights", right_text="© 2025 S&P Global.", show_copyright: bool = True):
        # Add left footnote
        fig.text(0.01, 0.01, left_text, ha='left', va='bottom', fontsize=7, fontfamily=self.font_family)
        # Add right footnote
        if show_copyright is True:
            fig.text(0.99, 0.01, right_text, ha='right', va='bottom', fontsize=7, fontfamily=self.font_family)

    def apply_legend_style(self, ax, loc='upper center', bbox_to_anchor=(0.5, 1.05), ncol=1):  # New method
        """Applies legend style and position."""
        legend = ax.legend(loc=loc, bbox_to_anchor=bbox_to_anchor, ncol=ncol) # bbox_to_anchor for outside positioning
        if legend: # Check if a legend was actually created
            plt.setp(legend.get_texts(), fontproperties=fm.FontProperties(family=self.font_family, size=self.font_size)) # Set font
            plt.setp(legend.get_title(), fontproperties=fm.FontProperties(family=self.font_family, size=self.font_size)) # Set title font
            # Optional: Set a background patch for the legend if needed
            # legend.get_frame().set_facecolor('lightgray') # Example


# folium map styles ======================================
def style_function(feature):
    return {
        # 'color': LISTS.SPG_COLORS[5],       # Line color (e.g., 'blue', 'green', etc.)
        'color': 'red',       # Line color (e.g., 'blue', 'green', etc.)
        'weight': 3,           # Line weight (thickness)
        'opacity': 0.7,        # Line opacity (0.0 to 1.0)
        # 'dashArray': '5, 5'    # Dashes in the line (optional)
    }

# Create a highlight function for mouseover effects
def highlight_function(feature):
    return {
        'color': 'red',        # Highlight color
        'weight': 5,           # Highlight weight
        'opacity': 1.0,        # Highlight opacity
        'dashArray': '5, 5'    # Highlight dash pattern (optional)
    }

PATH = paths()
TIMESTAMP = timestamps()
TOKEN = tokens()
LISTS = lists()

SpglobalStyle()