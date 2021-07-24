import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

Vue.use(Vuex)

const baseUrl = `http://localhost:8000`

export default new Vuex.Store({
  state: {
    event: null,
    members: [],
    cities: [],
    events: [],
    categories: []
  },
  getters: {
    getCategories: state => state.categories,
    getEvent: state => id => state.event.find(event => event.id === id),
    getEvents: state => state.events,
    getCities: state => state.cities,
    getMembers: state => state.members,
    getMember: state => id => state.members.find(member => member.id === id)
  },
  mutations: {
    UPDATE_EVENT: (state, event) => state.event = event,
    DELETE_EVENT: (state, id) =>
      state.events = state.events.filter(event => event.id != id),
    CREATE_EVENT: (state, newEvent) => state.events.push(newEvent),
    SET_CATEGORIES: (state, categories) => state.categories = categories,
    SET_EVENT: (state, event) => state.event = event,
    SET_EVENTS: (state, events) => state.events = events,
    // UPDATE_MEMBER: (state, id, data) => state.members = state.member.find(member => member.id == id),
    SET_CITIES: (state, cities) => state.cities = cities,
    SET_MEMBERS: (state, members) => state.members = members,
    ADD_MEMBER: (state, newMember) => state.members.push(newMember),
    DELETE_MEMBER: (state, id) =>
      state.members = state.members.filter(member => member.id != id)
  },
  actions: {
    updateEvent: ({ commit }, event) => {
      axios.put(`${baseUrl}/api/events/update/${event.id}/`, event)
        .then(response => {
          (commit('UPDATE_EVENT', response.data))
        })
        .catch(error => {
          console.log(error);
        })
    },
    removeEvent: ({ commit }, id) => {
      axios.delete(`${baseUrl}/api/events/destroy/${id}`)
        .then(() => {
          commit('DELETE_EVENT', id)
        })
    },
    createEvent: ({ commit }, newEvent) => {
      axios.post(`${baseUrl}/api/events/create/`, newEvent)
        .then(() => {
          (commit('CREATE_EVENT', newEvent))
        })
        .catch(error => {
          console.log(error);
        })
    },
    addCategories: ({ commit }) => {
      axios.get(`${baseUrl}/api/categories/`)
        .then(response => {
          commit('SET_CATEGORIES', response.data)
        })
    },
    addEvent: ({ commit }, eventId) => {
      axios.get(`${baseUrl}/api/events/${eventId}`)
        .then(response => {
          commit('SET_EVENT', response.data)
        })
        .catch(error => {
          console.log(error);
        })
    },
    addEvents: ({ commit }) => {
      axios.get(`${baseUrl}/api/events/`)
        .then(response => {
          commit('SET_EVENTS', response.data)
        })
    },
    // editMember: ({ commit }, id, data) => {
    //   axios.put(`${baseUrl}/api/members/update/${id}`, data)
    //     .then(() => {
    //       (commit('UPDATE_MEMBER', id, data))
    //     })
    //     .catch(error => {
    //       console.log(error);
    //     })
    // },
    addCities: ({ commit }) => {
      axios.get(`${baseUrl}/api/cities/`)
        .then(response => {
          commit('SET_CITIES', response.data)
        })
    },
    addMember: ({ commit }, newMember) => {
      axios.post(`${baseUrl}/api/members/create/`, newMember)
        .then(() => {
          (commit('ADD_MEMBER', newMember))
        })
        .catch(error => {
          console.log(error);
        })
    },
    addMembers: ({ commit }) => {
      axios.get(`${baseUrl}/api/members/`)
        .then(response => {
          commit('SET_MEMBERS', response.data)
        })
    },
    removeMember: ({ commit }, id) => {
      axios.delete(`${baseUrl}/api/members/destroy/${id}/`)
        .then(() => {
          commit('DELETE_MEMBER', id)
        })
    }
  },
  modules: {
  }
})
