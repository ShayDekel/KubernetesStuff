import json
import subprocess

""" 
    """
def main():

    try:
        """ The kubectl command to run for getting all the nodes in the cluster
            """ 
        command = "kubectl get all -o json" 

        """ Run the command previously mentioned and capture it's output to a list
            Using utf-8 to convert into string using utf-8 encoding
            """
        output_lst = subprocess.check_output(command.split()).decode("utf-8")

        """ Convert the list to a json format
            """
        data = json.loads(output_lst)

        if (len(output_lst) == 0):
            print("No workloads detected!")
            return 0

        """ Add each workload in the json format to a new list
            """
        workloads_output = []
        for element in data["items"]:
            current_workload = {
                "name": element["metadata"]["name"],
                "type": element["kind"],
                "namesapce": element["metadata"]["namespace"],
                "uid": element["metadata"]["uid"]
            }
            workloads_output.append(current_workload)

        """ Print all the workloads
            each having an individual line   
            """
        for workload in workloads_output:
            print(json.dumps(workload))

        """ Return the number of workloads detected
            """
        return len(workloads_output)
    
    except subprocess.CalledProcessError as error:
        print("Error trying to execute the following command: " + command)
        print(error)
        return -1

    except json.JSONDecodeError as error:
        print("Error trying to parse JSON output:")
        print(error)
        return -1

    except Exception as error:
        print("An error occured:")
        print(error)
        return -1

if __name__ == "__main__":
    main()
