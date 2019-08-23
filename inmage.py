#!/usr/bin/python
import requests, json


def getFacilities(state="CO"):
    return requests.get(
        "https://www.accesscorrections.com/api/facilities/GetFacilitiesByState/"
        + state
    ).json()


def nameSearch(subId, lastName, firstName=""):
    return requests.post(
        "https://www.accesscorrections.com/api/residents/GetResidentByName",
        headers={"Content-Type": "application/json"},
        data=json.dumps(
            {
                "SubscriberId": subId,
                "FirstName": firstName,
                "LastName": lastName,
                "MonthDOB": 0,
                "DayDOB": 0,
                "YearDOB": 0
            }
        )
    ).json()


def searchAll(state, lastName, firstName=""):
    facilities = getFacilities(state)
    if facilities["Error"] == 1:
        return
    for facility in facilities["FacilityData"]:
        for inmate in nameSearch(
            facility["SubscriberID"], lastName, firstName
        )["data"]:
            yield {
                "facility": facility["Name"],
                "first": inmate["firstName"],
                "last": inmate["lastName"],
                "middle": inmate["middleName"],
                "id": inmate["residentNum"]
            }


if __name__ == "__main__":
    import sys
    if len(sys.argv) < 3:
        print("usage: inmage <state> <last name> [first name]")
        print("example: inmage PA garcia")
        exit()
    for inmate in searchAll(
        sys.argv[1], sys.argv[2], sys.argv[3] if len(sys.argv) > 3 else ""
    ):
        print(
            "{0}\t{1}\t{2}\t{3}\t{4}".format(
                inmate["first"], inmate["middle"], inmate["last"],
                inmate["id"], inmate["facility"]
            )
        )
