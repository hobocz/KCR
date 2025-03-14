<script setup>
import { ref, onMounted } from "vue"
import PlayerBattingOPSChart from "./PlayerBattingOPSChart.vue"
import { AllCommunityModule, ModuleRegistry, themeBalham } from 'ag-grid-community'
ModuleRegistry.registerModules([AllCommunityModule])
import { AgGridVue } from "ag-grid-vue3"


const apiUrl = import.meta.env.VITE_API_URL
// AG Grid related data
const gridRef = ref(null);
const autoSizeStrategy = {
    type: 'fitGridWidth'
}
const rowSelection = { 
    mode: 'multiRow' ,
    headerCheckbox: false,
};
const selectionColumnDef = {
    sortable: true,
    resizable: false,
    width: 60
};
const columnDefs = ref([
    { field: "name_first", headerName: "First Name" },
    { field: "name_last", headerName: "Last Name", filter: true },
    { field: "name_use", headerName: "Use Name" },
    { field: "team", headerName: "Team", filter: true },
    { field: "birth_date", headerName: "Birth Date", filter: true },
    { field: "height_total", headerName: "Height" },
    { field: "weight", headerName: "Weight" },
    { field: "throws", headerName: "Throws", filter: true },
    { field: "bats", headerName: "Bats", filter: true },
    { field: "primary_position", headerName: "Primary Pos", filter: true },
]);
const rowData = ref([]);
const posNames = {
    "1": "Pitcher",
    "2": "Catcher",
    "3": "1st Base",
    "4": "2nd Base",
    "5": "3rd Base",
    "6": "Shortstop",
    "7": "Left Field",
    "8": "Center Field",
    "9": "Right Field",
    "O": "Offence",
    "D": "Defense",
}
// Reference to the exposed child data
const battingChartRef = ref(null);
const selectCount = ref(0)

// Here we retrieve the player data and assign it to the table "items"
onMounted(async () => {
    const response = await fetch(`${apiUrl}/players/`)
    const playerData = await response.json()
    rowData.value = playerData.map((player) => {
        return {
            id: player.id,
            name_first: player.name_first,
            name_last: player.name_last,
            name_use: `"${player.name_use}"`,
            team: player.team,
            birth_date: player.birth_date,
            // Use '!=' in the below ternary in order to get not null and not undefined
            height_total: `${player.height_feet}' - 
                ${player.height_inches != null ? player.height_inches : '?'}"`,
            weight: `${player.weight} lbs`,
            throws: player.throws,
            bats: player.bats,
            primary_position: `${player.primary_position ? player.primary_position
                 + " - " + posNames[player.primary_position] : "undefined"}`,
        }
    })
})

// Respond to AG Grid's selection-changed event. Updates the selected
// players in the child component
const onSelectionChanged = () => {
    const selectedRows = gridRef.value.api.getSelectedRows()
    selectCount.value = selectedRows.length
    battingChartRef.value.selectedPlayers = selectedRows
};
</script>

<template>
    <div class="componentContainer">
        <div id="tableContainer">
            <ag-grid-vue
                ref="gridRef"
                :rowData="rowData"
                :columnDefs="columnDefs"
                :autoSizeStrategy="autoSizeStrategy"
                :pagination="true"
                :paginationPageSize="25"
                :paginationPageSizeSelector="[25, 50, 100]"
                :theme="themeBalham"
                :rowSelection="rowSelection" 
                @selection-changed="onSelectionChanged"
                :selectionColumnDef="selectionColumnDef"
                style="height: 400px"
            >
            </ag-grid-vue>
        </div>
        <div class="tableNotes">Select players to compare OPS by year...</div>
        <div id="chartContainer" v-show="selectCount > 0">
            <PlayerBattingOPSChart ref="battingChartRef" />
        </div> 
    </div>
</template>

<style scoped>
.componentContainer{
    padding-left: 1em;
    padding-right: 1em;
    margin-bottom: 3em;
}
#tableContainer {
    border: .2em solid gray;
    border-radius: 5px;
}
#chartContainer {
    min-height: 200px;
    height: 300px;
}
.tableNotes {
    text-align: left;
    font-weight: bold;
    margin: .2em;
}
</style>