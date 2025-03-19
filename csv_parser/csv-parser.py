import re
from datetime import datetime
from dateutil import parser


class CsvParser():
    def __init__(self, delimiter = ",", linebreak = "\n", escape_char = "\"", with_header = True):
        self.delimiter = delimiter
        self.linebreak = linebreak
        self.escape_char = escape_char
        self.with_header = with_header
    
    def parse(self, filename):
        lines = self.__get_file_content(filename)
        keys = self.__get_keys(lines)     
        rows = self.__parse_rows(lines, keys)
        return self.__enforce_column_types(rows, keys)    
    
    def __parse_rows(self, lines, keys):
        rows = []
        for i in range(1 if self.with_header else 0, len(lines)):
            line = lines[i]
            row = {}
            try:
                parts = self.__split(line, self.delimiter)

                if len(keys) > len(parts):
                    print(f"Line '{i + 1}' is missing '{len(keys) - len(parts)}' fields. Double quotes may not be correctly escaped")    
                elif len(parts) > len(keys):
                    print(f"Line '{i + 1}' has '{len(parts) - len(keys)}' unexpected fields. Double quotes may not be correctly escaped")    
                
                for j in range(min(len(keys), len(parts))):
                    try:
                        item = self.__unescape_quotes(parts[j])
                        row[keys[j]] = self.__parse_item(item)
                    except Exception:
                        print(f"Error parsing field '{j + 1}' in line '{i + 1}'")     
            except Exception:
                print(f"Error parsing line '{i + 1}'")
            rows.append(row)
            
        return rows
    
    def __enforce_column_types(self, rows, keys):
        for key in keys:
            count = {}
            for row in rows:
                if key in row:
                    dtype = type(row[key])
                    if dtype in count:
                        count[dtype] += 1
                    else:
                        count[dtype] = 1
            
            if not count:
                continue
                        
            majority_dtype = max(count, key=count.get)            
            for i in range(len(rows)):
                row = rows[i]
                if key in row and not isinstance(row[key], majority_dtype):
                    try:
                        row[key] = self.__parse_item(row[key], target_type = majority_dtype)
                    except:
                        print(f"Failed to convert '{row[key]}' in line '{i + 1}' to majority data type '{majority_dtype}'")
                        del row[key]
        return rows
                    
    def __unescape_quotes(self, item):
        return re.sub(rf'^\ufeff{self.escape_char}|^{self.escape_char}|{self.escape_char}$', '', item).replace(self.escape_char + self.escape_char, self.escape_char)
    
    def __parse_item(self, item, target_type = None):        
        try:
            if not target_type or target_type is int:
                return int(item)
        except:
            if not target_type:
                pass
            else:
                raise ValueError(f"Failed to parse '{item}' to int")
        
        try:
            if not target_type or target_type is float:
                return float(item)
        except:
            if not target_type:
                pass
            else:
                raise ValueError(f"Failed to parse '{item}' to float")
        
        try:
            if not target_type or target_type is datetime:
                if isinstance(item, int):
                    return datetime.fromtimestamp(item)
                return parser.parse(item)
        except:
            if not target_type:
                pass
            else:
                raise ValueError(f"Failed to parse {item} to datetime")
        
        try:
            if item.lower() in ("true", "yes", "false", "no"):
                return bool(item)
        except:
            pass
        
        if not target_type:
            return item
        else:
            raise ValueError(f"Failed to parse '{item}'")
    
    def __get_file_content(self, filename):
        try:
            with open(filename, "r") as file:
                file = file.read()
        except FileNotFoundError as e:
            print(f"The file at '{filename}' was not found")
            raise FileNotFoundError(e)
        except Exception as e:
            print(f"An error occurred: '{e}'")
            raise Exception(e)
        
        lines = self.__split(file, self.linebreak)
        if len(lines) == 0:
            raise EOFError(f"File '{filename}' has no data")
        
        return lines

    def __split(self, content, delimiter):
        parts = list(content)
        result = []
        row = ""
        escaped = False
        for part in parts:
            if part == self.escape_char:
                row += part
                escaped = not escaped
            elif part == delimiter and not escaped:
                result.append(row)
                row = ""
            else:
                row += part
                
        if row != "":
            result.append(row)
        
        return result

    """
    Get output dictionary keys from header row. 
    If parser is in no-header mode, derive generic keys from first row of CSV data.
    If duplicate headers are detected, make them unique by appending a counter.
    """
    def __get_keys(self, lines):
        first_row = [self.__unescape_quotes(header) for header in lines[0].split(self.delimiter)]
        keys = []
        
        if self.with_header:
            header_count = {}
            for header in first_row:
                if header in header_count:
                    header_count[header] += 1
                    keys.append(f"{header}_{header_count[header]}")
                else:
                    header_count[header] = 1
                    keys.append(header)
            return keys
        else:
            for i in range(len(first_row)):
                keys[i] = f"Column {i + 1}"
            return keys
        
def print_csv_table(result):
    if not result:
        print("No results to display")
        return

    columns = build_columns(result)
    col_widths = build_column_widths(columns, result)

    header = "  ".join(str(col).ljust(col_widths[col]) for col in columns)
    print(header)
    print()

    for row in result:
        row_str = "  ".join(str(row.get(col, "")).ljust(col_widths[col]) for col in columns)
        print(row_str)

def build_columns(result):
    columns = set()
    for row in result:
        columns.update(row.keys())
    return datetime_to_front(columns)

def datetime_to_front(columns):
    if "DateTime" in columns:
        columns.remove("DateTime")
        sorted_columns = sorted(columns)
        return ["DateTime"] + sorted_columns
    else:
        return sorted(columns)

def build_column_widths(columns, result):
    col_widths = {}
    for col in columns:
        max_width = len(str(col))
        for row in result:
            cell = row.get(col, "")
            max_width = max(max_width, len(str(cell)))
        col_widths[col] = max_width
    return col_widths

def parse_csv(filename):
    csv_parser_class = CsvParser()
    result = csv_parser_class.parse(filename)
    return result

if __name__ == "__main__":
    filename = input("File path to parse\n\n")
    result = parse_csv(filename)
    print_csv_table(result)