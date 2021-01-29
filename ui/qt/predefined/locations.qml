pragma Singleton
import QtQuick 2.15

// Corresponds to model.entities.locations.LocationType
QtObject {
    id: singleton

    property int region: 1
    property int constellation: 2
    property int system: 3
    property int station: 4
}
